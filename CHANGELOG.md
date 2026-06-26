# Changelog

Todos los cambios notables de este proyecto se documentan en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es/1.1.0/).

## [2026-06-26]

### Añadido

- Repositorio inicial **MCDIA500 - Estadística Computacional (Grupo 6)** con avance incremental en `semana1/`, `semana2/` y `semana3/`.
- `README.md` en la raíz con:
  - Descripción del proyecto y dataset **Rain in Australia** (`weatherAUS.csv`).
  - Objetivo: predecir si lloverá al día siguiente según las observaciones del día actual.
  - Estructura esperada del proyecto (`data/`, `docs/`, `notebooks/`, `reports/`, `src/`).
  - Requisitos, instalación, uso de Jupyter, control de versiones y reproducibilidad.
- `.gitignore` en la raíz (entorno virtual, caché Python, checkpoints Jupyter, `.env`, logs, `.vscode`).
- En cada carpeta semanal:
  - `requirements.txt` con JupyterLab, notebook, ipykernel, pandas y numpy.
  - `LICENSE` (MIT, Copyright 2026 MagUnab).
  - `.gitignore` local con las mismas exclusiones que la raíz.
  - `README.md` con encabezado de la semana correspondiente.
- Estructura de carpetas con archivos `.gitkeep` para versionar directorios vacíos:
  - **semana1:** `data/`, `data/raw/`, `data/processed/`, `docs/`, `notebooks/`, `src/`.
  - **semana2:** `data/`, `data/processed/`, `docs/`, `notebooks/`, `src/`.
  - **semana3:** `data/`, `data/processed/`, `docs/`, `notebooks/`, `src/`.
- Dataset `semana1/data/raw/weatherAUS.csv` (~145.000 registros de observaciones meteorológicas en Australia).
- Repositorio Git inicializado con rama `main` y remoto `https://github.com/edocontreras/mcdia500-estadistica-computacional-g6.git`.

### Pendiente / observaciones

- `Changelog.md` referenciado en el README raíz aún no existe en el repositorio.
- `semana2/` y `semana3/` no incluyen aún el dataset en `data/raw/`.
- No hay carpetas `reports/` ni notebooks (`.ipynb`) en ninguna semana.
- Los `requirements.txt` conservan comentarios del curso anterior (*Programación Ciencia de Datos* / datos clínicos).
- El README raíz aún referencia el repositorio antiguo `MagUnab/mcdia500-programacion-cd-g6` en los ejemplos de clonación.
- Typo en el README raíz: *"El objetivo bjetivo es predecir..."*.