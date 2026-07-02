from __future__ import annotations

import math

import numpy as np
import pandas as pd
from scipy import stats


def _clean_numeric(x: np.ndarray) -> np.ndarray:
    """Convierte un arreglo a tipo float y elimina valores no finitos."""
    x = np.asarray(x, dtype=float)
    return x[np.isfinite(x)]


def _validate_min_size(x: np.ndarray, min_size: int, name: str) -> None:
    """Valida que un arreglo tenga el tamaño mínimo requerido."""
    if x.size < min_size:
        raise ValueError(f'{name} requiere al menos {min_size} observaciones válidas; se recibieron {x.size}.')


def normal_ci_mean(x: np.ndarray, alpha: float = 0.05) -> tuple[float, float, float]:
    """Calcula estimación puntual e intervalo de confianza clásico para una media."""
    x = _clean_numeric(x)
    _validate_min_size(x, 2, 'normal_ci_mean')

    n = x.size
    mean = float(np.mean(x))
    se = float(np.std(x, ddof=1) / np.sqrt(n))
    tcrit = float(stats.t.ppf(1 - alpha / 2, n - 1))

    return mean, mean - tcrit * se, mean + tcrit * se


def normal_ci_proportion(x: np.ndarray, alpha: float = 0.05) -> tuple[float, float, float]:
    """Calcula estimación puntual e intervalo de confianza normal para una proporción."""
    x = _clean_numeric(x)
    _validate_min_size(x, 2, 'normal_ci_proportion')

    n = x.size
    p = float(np.mean(x))
    zcrit = float(stats.norm.ppf(1 - alpha / 2))
    se = math.sqrt(p * (1 - p) / n)

    return p, max(0.0, p - zcrit * se), min(1.0, p + zcrit * se)


def welch_ci_difference(
    x_yes: np.ndarray,
    x_no: np.ndarray,
    alpha: float = 0.05,
) -> tuple[float, float, float, float]:
    """Calcula diferencia de medias e intervalo de confianza mediante aproximación de Welch."""
    x_yes = _clean_numeric(x_yes)
    x_no = _clean_numeric(x_no)
    _validate_min_size(x_yes, 2, 'welch_ci_difference: grupo yes')
    _validate_min_size(x_no, 2, 'welch_ci_difference: grupo no')

    n1, n0 = x_yes.size, x_no.size
    m1, m0 = np.mean(x_yes), np.mean(x_no)
    v1, v0 = np.var(x_yes, ddof=1), np.var(x_no, ddof=1)

    se = math.sqrt(v1 / n1 + v0 / n0)
    numerator = (v1 / n1 + v0 / n0) ** 2
    denominator = ((v1 / n1) ** 2 / (n1 - 1)) + ((v0 / n0) ** 2 / (n0 - 1))
    df = numerator / denominator

    diff = float(m1 - m0)
    tcrit = float(stats.t.ppf(1 - alpha / 2, df))

    return diff, diff - tcrit * se, diff + tcrit * se, float(df)


def cohens_d_independent(x1: np.ndarray, x0: np.ndarray) -> float:
    """Calcula Cohen d para dos grupos independientes usando desviación estándar combinada."""
    x1 = _clean_numeric(x1)
    x0 = _clean_numeric(x0)
    _validate_min_size(x1, 2, 'cohens_d_independent: grupo 1')
    _validate_min_size(x0, 2, 'cohens_d_independent: grupo 0')

    n1, n0 = x1.size, x0.size
    s1, s0 = np.var(x1, ddof=1), np.var(x0, ddof=1)
    pooled = math.sqrt(((n1 - 1) * s1 + (n0 - 1) * s0) / (n1 + n0 - 2))

    if pooled == 0:
        return np.nan

    return float((np.mean(x1) - np.mean(x0)) / pooled)


def bootstrap_mean(
    x: np.ndarray,
    n_boot: int,
    rng: np.random.Generator,
    batch_size: int = 250,
    sample_size: int | None = None,
) -> np.ndarray:
    """Genera una distribución bootstrap para la media."""
    x = _clean_numeric(x)
    _validate_min_size(x, 2, 'bootstrap_mean')

    n = x.size
    m = n if sample_size is None else min(int(sample_size), n)
    _validate_min_size(np.empty(m), 2, 'bootstrap_mean: sample_size')

    out = np.empty(n_boot, dtype=float)
    start = 0

    while start < n_boot:
        b = min(batch_size, n_boot - start)
        idx = rng.integers(0, n, size=(b, m), endpoint=False)
        out[start:start + b] = x[idx].mean(axis=1)
        start += b

    return out


def bootstrap_proportion(
    x: np.ndarray,
    n_boot: int,
    rng: np.random.Generator,
    batch_size: int = 250,
    sample_size: int | None = None,
) -> np.ndarray:
    """Genera una distribución bootstrap para una proporción codificada como 0/1."""
    return bootstrap_mean(
        x,
        n_boot=n_boot,
        rng=rng,
        batch_size=batch_size,
        sample_size=sample_size,
    )


def bootstrap_difference_means(
    x_yes: np.ndarray,
    x_no: np.ndarray,
    n_boot: int,
    rng: np.random.Generator,
    batch_size: int = 250,
    sample_size_yes: int | None = None,
    sample_size_no: int | None = None,
) -> np.ndarray:
    """Genera una distribución bootstrap para la diferencia de medias entre dos grupos."""
    x_yes = _clean_numeric(x_yes)
    x_no = _clean_numeric(x_no)
    _validate_min_size(x_yes, 2, 'bootstrap_difference_means: grupo yes')
    _validate_min_size(x_no, 2, 'bootstrap_difference_means: grupo no')

    n1, n0 = x_yes.size, x_no.size
    m1 = n1 if sample_size_yes is None else min(int(sample_size_yes), n1)
    m0 = n0 if sample_size_no is None else min(int(sample_size_no), n0)

    if m1 < 2 or m0 < 2:
        raise ValueError('bootstrap_difference_means requiere al menos 2 observaciones por grupo en cada remuestra.')

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
    """Calcula los valores jackknife asociados a una media."""
    x = _clean_numeric(x)
    _validate_min_size(x, 2, 'jackknife_mean_values')

    n = x.size
    total = np.sum(x)

    return (total - x) / (n - 1)


def jackknife_difference_means_values(x_yes: np.ndarray, x_no: np.ndarray) -> np.ndarray:
    """Calcula valores jackknife para una diferencia de medias entre dos grupos."""
    x_yes = _clean_numeric(x_yes)
    x_no = _clean_numeric(x_no)
    _validate_min_size(x_yes, 2, 'jackknife_difference_means_values: grupo yes')
    _validate_min_size(x_no, 2, 'jackknife_difference_means_values: grupo no')

    n1, n0 = x_yes.size, x_no.size
    s1, s0 = np.sum(x_yes), np.sum(x_no)
    m1, m0 = np.mean(x_yes), np.mean(x_no)

    jk_yes = (s1 - x_yes) / (n1 - 1) - m0
    jk_no = m1 - (s0 - x_no) / (n0 - 1)

    return np.concatenate([jk_yes, jk_no])


def bca_interval(
    theta_hat: float,
    boot: np.ndarray,
    jackknife: np.ndarray,
    alpha: float = 0.05,
) -> tuple[float, float]:
    """Calcula intervalo de confianza BCa a partir de distribución bootstrap y valores jackknife."""
    boot = _clean_numeric(boot)
    jackknife = _clean_numeric(jackknife)
    _validate_min_size(boot, 10, 'bca_interval: distribución bootstrap')
    _validate_min_size(jackknife, 2, 'bca_interval: valores jackknife')

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

    denom_low = 1 - acceleration * (z0 + z_low)
    denom_high = 1 - acceleration * (z0 + z_high)

    if denom_low == 0 or denom_high == 0:
        return percentile_interval(boot, alpha=alpha)

    adj_low = stats.norm.cdf(z0 + (z0 + z_low) / denom_low)
    adj_high = stats.norm.cdf(z0 + (z0 + z_high) / denom_high)

    adj_low = float(np.clip(adj_low, 0, 1))
    adj_high = float(np.clip(adj_high, 0, 1))

    return float(np.quantile(boot, adj_low)), float(np.quantile(boot, adj_high))


def percentile_interval(boot: np.ndarray, alpha: float = 0.05) -> tuple[float, float]:
    """Calcula intervalo de confianza bootstrap por método percentil."""
    boot = _clean_numeric(boot)
    _validate_min_size(boot, 10, 'percentile_interval')

    return float(np.quantile(boot, alpha / 2)), float(np.quantile(boot, 1 - alpha / 2))


def permutation_difference_means(
    pooled: np.ndarray,
    n_yes: int,
    n_perm: int,
    rng: np.random.Generator,
    sample_size: int | None = None,
) -> np.ndarray:
    """Genera una distribución nula por permutación para la diferencia de medias."""
    pooled = _clean_numeric(pooled)
    _validate_min_size(pooled, 4, 'permutation_difference_means')

    n_full = pooled.size

    if n_yes <= 1 or n_yes >= n_full - 1:
        raise ValueError('permutation_difference_means requiere grupos con al menos 2 observaciones.')

    if sample_size is not None and sample_size < n_full:
        sample_size = int(sample_size)

        if sample_size < 4:
            raise ValueError('sample_size debe ser al menos 4 para la prueba de permutación.')

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


def bootstrap_correlation(
    x: np.ndarray,
    y: np.ndarray,
    n_boot: int,
    rng: np.random.Generator,
    batch_size: int = 300,
    sample_size: int | None = None,
) -> np.ndarray:
    """Genera una distribución bootstrap para el coeficiente de correlación de Pearson."""
    arr = np.column_stack([x, y]).astype(float)
    arr = arr[np.isfinite(arr).all(axis=1)]

    n = arr.shape[0]
    if n < 3:
        raise ValueError('bootstrap_correlation requiere al menos 3 pares válidos.')

    m = n if sample_size is None else min(int(sample_size), n)
    if m < 3:
        raise ValueError('bootstrap_correlation requiere remuestras con al menos 3 pares válidos.')

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
        numerator = np.sum(sx_c * sy_c, axis=1)

        corr = np.full(b, np.nan, dtype=float)
        valid = denom > 0
        corr[valid] = numerator[valid] / denom[valid]

        out[start:start + b] = corr
        start += b

    return out[np.isfinite(out)]


def iqr_filter(x: np.ndarray) -> np.ndarray:
    """Elimina valores extremos utilizando la regla 1,5 veces el rango intercuartílico."""
    x = _clean_numeric(x)
    _validate_min_size(x, 4, 'iqr_filter')

    q1, q3 = np.quantile(x, [0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    return x[(x >= lower) & (x <= upper)]


def winsorize_array(
    x: np.ndarray,
    lower_q: float = 0.01,
    upper_q: float = 0.99,
) -> np.ndarray:
    """Aplica winsorización según cuantiles inferior y superior."""
    x = _clean_numeric(x)
    _validate_min_size(x, 2, 'winsorize_array')

    if not 0 <= lower_q < upper_q <= 1:
        raise ValueError('Los cuantiles de winsorización deben cumplir 0 <= lower_q < upper_q <= 1.')

    lo, hi = np.quantile(x, [lower_q, upper_q])

    return np.clip(x, lo, hi)


def bootstrap_median_difference(
    x_yes: np.ndarray,
    x_no: np.ndarray,
    n_boot: int,
    rng: np.random.Generator,
    batch_size: int = 250,
    sample_size_yes: int | None = None,
    sample_size_no: int | None = None,
) -> np.ndarray:
    """Genera una distribución bootstrap para la diferencia de medianas entre dos grupos."""
    x_yes = _clean_numeric(x_yes)
    x_no = _clean_numeric(x_no)
    _validate_min_size(x_yes, 2, 'bootstrap_median_difference: grupo yes')
    _validate_min_size(x_no, 2, 'bootstrap_median_difference: grupo no')

    n1, n0 = x_yes.size, x_no.size
    m1 = n1 if sample_size_yes is None else min(int(sample_size_yes), n1)
    m0 = n0 if sample_size_no is None else min(int(sample_size_no), n0)

    if m1 < 2 or m0 < 2:
        raise ValueError('bootstrap_median_difference requiere al menos 2 observaciones por grupo en cada remuestra.')

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
    """Formatea un valor numérico con cantidad fija de decimales."""
    if pd.isna(value):
        return ''

    return f'{float(value):.{decimals}f}'
