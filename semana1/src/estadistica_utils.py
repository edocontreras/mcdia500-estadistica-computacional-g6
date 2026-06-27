"""Funciones auxiliares para la Formativa 1 - Grupo 6.

Este módulo agrupa funciones estadísticas reutilizables para el análisis
exploratorio e inferencial del dataset Rain in Australia.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


def media_ic_t(serie: pd.Series, confianza: float = 0.95) -> dict:
    """Calcula media, desviación estándar, error estándar e intervalo t-Student."""
    x = pd.Series(serie).dropna().astype(float)
    n = int(x.shape[0])

    if n < 2:
        raise ValueError(
            "Se requieren al menos 2 observaciones válidas para calcular el intervalo."
        )

    media = float(x.mean())
    sd = float(x.std(ddof=1))
    se = sd / np.sqrt(n)
    alpha = 1 - confianza
    tcrit = float(stats.t.ppf(1 - alpha / 2, n - 1))

    return {
        "n": n,
        "media": media,
        "sd": sd,
        "se": float(se),
        "ic_inf": float(media - tcrit * se),
        "ic_sup": float(media + tcrit * se),
    }


def proporcion_ic_wilson(exitos: int, n: int, confianza: float = 0.95) -> dict:
    """Calcula estimación puntual e intervalo de Wilson para una proporción."""
    exitos = int(exitos)
    n = int(n)

    if n <= 0:
        raise ValueError("n debe ser mayor que cero.")

    phat = exitos / n
    z = float(stats.norm.ppf(1 - (1 - confianza) / 2))

    denominador = 1 + z**2 / n
    centro = (phat + z**2 / (2 * n)) / denominador
    semiamplitud = (
        z
        * np.sqrt((phat * (1 - phat) / n) + (z**2 / (4 * n**2)))
        / denominador
    )

    return {
        "n": n,
        "exitos": exitos,
        "proporcion": float(phat),
        "ic_inf": float(centro - semiamplitud),
        "ic_sup": float(centro + semiamplitud),
    }


def cohens_d_independiente(x1: pd.Series, x0: pd.Series) -> float:
    """Calcula Cohen d para dos grupos independientes con desviación combinada."""
    a = pd.Series(x1).dropna().astype(float)
    b = pd.Series(x0).dropna().astype(float)

    n1 = len(a)
    n0 = len(b)

    if n1 < 2 or n0 < 2:
        raise ValueError("Cada grupo requiere al menos 2 observaciones válidas.")

    s1 = a.var(ddof=1)
    s0 = b.var(ddof=1)
    sp = np.sqrt(((n1 - 1) * s1 + (n0 - 1) * s0) / (n1 + n0 - 2))

    return float((a.mean() - b.mean()) / sp)


def resolver_raiz_proyecto(cwd: str | None = None) -> Path:
    """Resuelve la carpeta semana1 desde el notebook o desde el repositorio."""
    current = Path.cwd() if cwd is None else Path(cwd)

    candidates = [
        current,
        current.parent,
        current.parent.parent,
        current / "semana1",
        current.parent / "semana1",
    ]

    for candidate in candidates:
        if (candidate / "data" / "raw" / "weatherAUS.csv").exists():
            return candidate

    matches = list(current.rglob("weatherAUS.csv"))

    if not matches and current.parent.exists():
        matches = list(current.parent.rglob("weatherAUS.csv"))

    if matches:
        weather_path = matches[0]

        if weather_path.parent.name == "raw" and weather_path.parent.parent.name == "data":
            return weather_path.parent.parent.parent

        return weather_path.parent

    raise FileNotFoundError(
        "No se encontró weatherAUS.csv en data/raw ni en rutas cercanas."
    )
