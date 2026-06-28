# Semana 1 - Formativa 1

## Análisis exploratorio e inferencial del dataset *Rain in Australia*

**Integrantes:** Eduardo Contreras; Gonzalo Bouldres; Luis Díaz Giral
**Docente:** Dr. Jean Paul Maidana González
**Curso:** MCDI501 - Estadística Computacional para la Toma de Decisiones

## Objetivo de la entrega

El objetivo de esta entrega es desarrollar un análisis estadístico inicial sobre observaciones meteorológicas diarias de Australia, con énfasis en la variable `RainTomorrow`, que indica si llueve o no al día siguiente.

El análisis considera una revisión exploratoria de la base de datos, auditoría de valores faltantes, estadística descriptiva, análisis gráfico, matriz de correlación, intervalos de confianza y pruebas de hipótesis aplicadas a variables meteorológicas relevantes.

## Entregables

La estructura principal de la Semana 1 es la siguiente:

```text
semana1/
├── data/
│   ├── raw/
│   │   └── weatherAUS.csv
│   └── processed/
│       └── weatherAUS_formativa1_variables_clave.csv
├── docs/
│   ├── informe_formativa1_rain_australia.pdf
│   ├── informe_formativa1_rain_australia.tex
│   ├── inventario_outputs_formativa1.csv
│   ├── figures/
│   └── tables/
├── notebooks/
│   └── Formativa1_Rain_Australia_G6.ipynb
├── src/
│   └── estadistica_utils.py
└── requirements.txt
```

## Salidas generadas

El notebook genera y organiza los principales resultados en la carpeta `docs/`, considerando:

* 15 tablas en formato `.csv`, almacenadas en `docs/tables/`.
* 9 figuras en formato `.png`, almacenadas en `docs/figures/`.
* 1 inventario de salidas, disponible en `docs/inventario_outputs_formativa1.csv`.
* 1 informe técnico en formato `.pdf`, ubicado en `docs/informe_formativa1_rain_australia.pdf`.

## Alcance estadístico

La entrega desarrolla los siguientes componentes:

* Descripción general del dataset y de la variable objetivo.
* Auditoría de datos faltantes.
* Segmentación de variables según tipo y relevancia analítica.
* Estadística descriptiva de variables meteorológicas clave.
* Matriz de correlación de Pearson entre variables numéricas seleccionadas.
* Visualización exploratoria mediante histogramas, boxplots y gráficos de barras.
* Estimación puntual e intervalos de confianza.
* Prueba de hipótesis principal mediante t de Welch.
* Prueba chi-cuadrado complementaria para variables categóricas.
* Estimación de probabilidades condicionales asociadas a lluvia observada y lluvia al día siguiente.
* Interpretación preliminar de resultados y limitaciones del análisis.

## Ejecución del notebook

Desde la carpeta `semana1`, crear y activar un entorno virtual:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Luego instalar las dependencias:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Finalmente, iniciar JupyterLab:

```bash
python -m jupyterlab --ServerApp.use_redirect_file=False
```

Abrir el notebook:

```text
notebooks/Formativa1_Rain_Australia_G6.ipynb
```

## Reproducibilidad

Para mantener la reproducibilidad del análisis, el archivo original `weatherAUS.csv` debe permanecer en la siguiente ruta:

```text
semana1/data/raw/weatherAUS.csv
```

Al ejecutar el notebook completo, se actualizan las salidas procesadas en:

```text
semana1/data/processed/
semana1/docs/tables/
semana1/docs/figures/
```

El archivo `inventario_outputs_formativa1.csv` resume las tablas y figuras generadas durante el análisis.

