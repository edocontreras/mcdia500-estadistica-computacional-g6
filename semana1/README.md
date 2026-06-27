# Semana 1 - Formativa 1

## Análisis exploratorio e inferencial del dataset Rain in Australia

**Integrantes:** Eduardo Contreras; Gonzalo Bouldres; Luis Díaz Giral  
**Docente:** Dr. Jean Paul Maidana González  
**Curso:** MCDI501 - Estadística Computacional para la Toma de Decisiones

El objetivo de esta entrega es desarrollar un análisis estadístico inicial sobre observaciones meteorológicas diarias de Australia, con énfasis en la variable `RainTomorrow`, que indica si llueve o no al día siguiente.

## Entregables

```text
semana1/
├── data/raw/weatherAUS.csv
├── data/processed/weatherAUS_formativa1_variables_clave.csv
├── docs/informe_formativa1_rain_australia.pdf
├── docs/informe_formativa1_rain_australia.tex
├── docs/figures/
├── docs/tables/
├── notebooks/Formativa1_Rain_Australia_G6.ipynb
├── src/estadistica_utils.py
└── requirements.txt
```

## Alcance estadístico

La entrega desarrolla los siguientes componentes:

- Descripción general del dataset y de la variable objetivo.
- Auditoría de datos faltantes.
- Estadística descriptiva de variables meteorológicas clave.
- Estimación puntual e intervalos de confianza.
- Prueba de hipótesis principal mediante t de Welch.
- Prueba chi-cuadrado complementaria para variables categóricas.
- Interpretación preliminar de resultados y limitaciones.

## Ejecución del notebook

Desde la carpeta `semana1`:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m jupyterlab --ServerApp.use_redirect_file=False
```

Luego abrir:

```text
notebooks/Formativa1_Rain_Australia_G6.ipynb
```

El archivo `weatherAUS.csv` debe permanecer en `semana1/data/raw/` para mantener la reproducibilidad del análisis.


