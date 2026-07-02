from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable, Iterable

import numpy as np
import pandas as pd
from scipy import stats


@dataclass(frozen=True)
class IntervalResult:
    estimate: float
    lower: float
    upper: float
    method: str


def normal_ci_mean(x: np.ndarray, alpha: float = 0.05) -> tuple[float, float, float]:
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    n = x.size
    mean = float(np.mean(x))
    se = float(np.std(x, ddof=1) / np.sqrt(n))
    tcrit = float(stats.t.ppf(1 - alpha / 2, n - 1))
    return mean, mean - tcrit * se, mean + tcrit * se


def normal_ci_proportion(x: np.ndarray, alpha: float = 0.05) -> tuple[float, float, float]:
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    n = x.size
    p = float(np.mean(x))
    zcrit = float(stats.norm.ppf(1 - alpha / 2))
    se = math.sqrt(p * (1 - p) / n)
    return p, max(0.0, p - zcrit * se), min(1.0, p + zcrit * se)


def welch_ci_difference(x_yes: np.ndarray, x_no: np.ndarray, alpha: float = 0.05) -> tuple[float, float, float, float]:
    x_yes = np.asarray(x_yes, dtype=float)
    x_no = np.asarray(x_no, dtype=float)
    x_yes = x_yes[np.isfinite(x_yes)]
    x_no = x_no[np.isfinite(x_no)]
    n1, n0 = x_yes.size, x_no.size
    m1, m0 = np.mean(x_yes), np.mean(x_no)
    v1, v0 = np.var(x_yes, ddof=1), np.var(x_no, ddof=1)
    se = math.sqrt(v1 / n1 + v0 / n0)
    df = (v1 / n1 + v0 / n0) ** 2 / ((v1 / n1) ** 2 / (n1 - 1) + (v0 / n0) ** 2 / (n0 - 1))
    diff = float(m1 - m0)
    tcrit = float(stats.t.ppf(1 - alpha / 2, df))
    return diff, diff - tcrit * se, diff + tcrit * se, float(df)


def cohens_d_independent(x1: np.ndarray, x0: np.ndarray) -> float:
    x1 = np.asarray(x1, dtype=float)
    x0 = np.asarray(x0, dtype=float)
    x1 = x1[np.isfinite(x1)]
    x0 = x0[np.isfinite(x0)]
    n1, n0 = x1.size, x0.size
    s1, s0 = np.var(x1, ddof=1), np.var(x0, ddof=1)
    pooled = math.sqrt(((n1 - 1) * s1 + (n0 - 1) * s0) / (n1 + n0 - 2))
    return float((np.mean(x1) - np.mean(x0)) / pooled)


def bootstrap_mean(x: np.ndarray, n_boot: int, rng: np.random.Generator, batch_size: int = 250, sample_size: int | None = None) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    n = x.size
    m = n if sample_size is None else min(int(sample_size), n)
    out = np.empty(n_boot, dtype=float)
    start = 0
    while start < n_boot:
        b = min(batch_size, n_boot - start)
        idx = rng.integers(0, n, size=(b, m), endpoint=False)
        out[start:start + b] = x[idx].mean(axis=1)
        start += b
    return out


def bootstrap_proportion(x: np.ndarray, n_boot: int, rng: np.random.Generator, batch_size: int = 250, sample_size: int | None = None) -> np.ndarray:
    return bootstrap_mean(x, n_boot=n_boot, rng=rng, batch_size=batch_size, sample_size=sample_size)


def bootstrap_difference_means(x_yes: np.ndarray, x_no: np.ndarray, n_boot: int, rng: np.random.Generator, batch_size: int = 250, sample_size_yes: int | None = None, sample_size_no: int | None = None) -> np.ndarray:
    x_yes = np.asarray(x_yes, dtype=float)
    x_no = np.asarray(x_no, dtype=float)
    x_yes = x_yes[np.isfinite(x_yes)]
    x_no = x_no[np.isfinite(x_no)]
    n1, n0 = x_yes.size, x_no.size
    m1 = n1 if sample_size_yes is None else min(int(sample_size_yes), n1)
    m0 = n0 if sample_size_no is None else min(int(sample_size_no), n0)
    out = np.empty(n_boot, dtype=float)
    start = 0
    while start < n_boot:
        b = min(batch_size, n_boot - start)
        idx1 = rng.integers(0, n1, size=(b, m1), endpoint=False)
        idx0 = rng.integers(0, n0, size=(b, m0), endpoint=False)
        out[start:start + b] = x_yes[idx1].mean(axis=1) - x_no[idx0].mean(axis=1)
        start += b
    return out


def jackknife_mean_values(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    n = x.size
    total = np.sum(x)
    return (total - x) / (n - 1)


def jackknife_difference_means_values(x_yes: np.ndarray, x_no: np.ndarray) -> np.ndarray:
    x_yes = np.asarray(x_yes, dtype=float)
    x_no = np.asarray(x_no, dtype=float)
    x_yes = x_yes[np.isfinite(x_yes)]
    x_no = x_no[np.isfinite(x_no)]
    n1, n0 = x_yes.size, x_no.size
    s1, s0 = np.sum(x_yes), np.sum(x_no)
    m1, m0 = np.mean(x_yes), np.mean(x_no)
    jk_yes = (s1 - x_yes) / (n1 - 1) - m0
    jk_no = m1 - (s0 - x_no) / (n0 - 1)
    return np.concatenate([jk_yes, jk_no])


def bca_interval(theta_hat: float, boot: np.ndarray, jackknife: np.ndarray, alpha: float = 0.05) -> tuple[float, float]:
    boot = np.asarray(boot, dtype=float)
    jackknife = np.asarray(jackknife, dtype=float)
    boot = boot[np.isfinite(boot)]
    jackknife = jackknife[np.isfinite(jackknife)]
    b = boot.size
    prop_less = np.mean(boot < theta_hat)
    prop_less = np.clip(prop_less, 1 / (b + 1), b / (b + 1))
    z0 = stats.norm.ppf(prop_less)
    jk_mean = np.mean(jackknife)
    diffs = jk_mean - jackknife
    denom = 6.0 * (np.sum(diffs ** 2) ** 1.5)
    acceleration = 0.0 if denom == 0 else float(np.sum(diffs ** 3) / denom)
    z_low = stats.norm.ppf(alpha / 2)
    z_high = stats.norm.ppf(1 - alpha / 2)
    adj_low = stats.norm.cdf(z0 + (z0 + z_low) / (1 - acceleration * (z0 + z_low)))
    adj_high = stats.norm.cdf(z0 + (z0 + z_high) / (1 - acceleration * (z0 + z_high)))
    adj_low = float(np.clip(adj_low, 0, 1))
    adj_high = float(np.clip(adj_high, 0, 1))
    return float(np.quantile(boot, adj_low)), float(np.quantile(boot, adj_high))


def percentile_interval(boot: np.ndarray, alpha: float = 0.05) -> tuple[float, float]:
    return float(np.quantile(boot, alpha / 2)), float(np.quantile(boot, 1 - alpha / 2))


def permutation_difference_means(pooled: np.ndarray, n_yes: int, n_perm: int, rng: np.random.Generator, sample_size: int | None = None) -> np.ndarray:
    pooled = np.asarray(pooled, dtype=float)
    pooled = pooled[np.isfinite(pooled)]
    n_full = pooled.size
    if sample_size is not None and sample_size < n_full:
        sample_size = int(sample_size)
        idx_base = rng.choice(n_full, size=sample_size, replace=False)
        pooled = pooled[idx_base]
        n = pooled.size
        n_yes_eff = max(2, min(n - 2, int(round(n_yes / n_full * n))))
    else:
        n = n_full
        n_yes_eff = n_yes
    total = float(np.sum(pooled))
    out = np.empty(n_perm, dtype=float)
    for i in range(n_perm):
        idx_yes = rng.choice(n, size=n_yes_eff, replace=False)
        sum_yes = float(np.sum(pooled[idx_yes]))
        mean_yes = sum_yes / n_yes_eff
        mean_no = (total - sum_yes) / (n - n_yes_eff)
        out[i] = mean_yes - mean_no
    return out


def bootstrap_correlation(x: np.ndarray, y: np.ndarray, n_boot: int, rng: np.random.Generator, batch_size: int = 300, sample_size: int | None = None) -> np.ndarray:
    arr = np.column_stack([x, y]).astype(float)
    arr = arr[np.isfinite(arr).all(axis=1)]
    n = arr.shape[0]
    m = n if sample_size is None else min(int(sample_size), n)
    out = np.empty(n_boot, dtype=float)
    start = 0
    while start < n_boot:
        b = min(batch_size, n_boot - start)
        idx = rng.integers(0, n, size=(b, m), endpoint=False)
        sample = arr[idx]
        sx = sample[:, :, 0]
        sy = sample[:, :, 1]
        sx_c = sx - sx.mean(axis=1, keepdims=True)
        sy_c = sy - sy.mean(axis=1, keepdims=True)
        denom = np.sqrt(np.sum(sx_c ** 2, axis=1) * np.sum(sy_c ** 2, axis=1))
        out[start:start + b] = np.sum(sx_c * sy_c, axis=1) / denom
        start += b
    return out


def iqr_filter(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    q1, q3 = np.quantile(x, [0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return x[(x >= lower) & (x <= upper)]


def winsorize_array(x: np.ndarray, lower_q: float = 0.01, upper_q: float = 0.99) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    lo, hi = np.quantile(x, [lower_q, upper_q])
    return np.clip(x, lo, hi)


def bootstrap_median_difference(x_yes: np.ndarray, x_no: np.ndarray, n_boot: int, rng: np.random.Generator, batch_size: int = 250, sample_size_yes: int | None = None, sample_size_no: int | None = None) -> np.ndarray:
    x_yes = np.asarray(x_yes, dtype=float)
    x_no = np.asarray(x_no, dtype=float)
    x_yes = x_yes[np.isfinite(x_yes)]
    x_no = x_no[np.isfinite(x_no)]
    n1, n0 = x_yes.size, x_no.size
    m1 = n1 if sample_size_yes is None else min(int(sample_size_yes), n1)
    m0 = n0 if sample_size_no is None else min(int(sample_size_no), n0)
    out = np.empty(n_boot, dtype=float)
    start = 0
    while start < n_boot:
        b = min(batch_size, n_boot - start)
        idx1 = rng.integers(0, n1, size=(b, m1), endpoint=False)
        idx0 = rng.integers(0, n0, size=(b, m0), endpoint=False)
        out[start:start + b] = np.median(x_yes[idx1], axis=1) - np.median(x_no[idx0], axis=1)
        start += b
    return out


def format_float(value: float, decimals: int = 4) -> str:
    if pd.isna(value):
        return ''
    return f'{float(value):.{decimals}f}'
