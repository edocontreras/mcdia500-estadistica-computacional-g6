# MCDI501 - Estadística Computacional para la Toma de Decisiones

## Descripción del proyecto

El proyecto utiliza el dataset **Rain in Australia** (`weatherAUS`) para analizar variables meteorológicas diarias registradas en distintas localidades de Australia y estudiar su relación con la ocurrencia de lluvia al día siguiente, representada por la variable `RainTomorrow`.

El repositorio organiza el trabajo por semanas, manteniendo trazabilidad entre datos originales, datos de entrada de cada fase, datos procesados, notebooks, funciones auxiliares, tablas, figuras e informes técnicos. La Semana 1 desarrolla análisis exploratorio e inferencial; la Semana 2 valida esos resultados mediante remuestreo, permutación, simulación Monte Carlo y análisis de robustez; la Semana 3 queda preparada para modelamiento predictivo integrado.

## Estructura del repositorio

```text
mcdia500-estadistica-computacional-g6-main/
├── semana1/
│   ├── data/
│   ├── docs/
│   ├── notebooks/
│   ├── src/
│   ├── README.md
│   └── requirements.txt
├── semana2/
│   ├── data/
│   │   ├── input/
│   │   ├── raw/
│   │   └── processed/
│   ├── docs/
│   ├── notebooks/
│   ├── src/
│   ├── README.md
│   └── requirements.txt
├── semana3/
│   ├── data/
│   ├── docs/
│   ├── notebooks/
│   ├── src/
│   ├── README.md
│   └── requirements.txt
├── README.md
├── CHANGELOG.md
└── .gitignore
```

## Avance por semana

### Semana 1 - Sumativa 1

La carpeta `semana1/` contiene el análisis exploratorio e inferencial inicial del dataset `weatherAUS`. El producto principal es el notebook `Sumativa1_Rain_Australia_G6.ipynb`, junto con la base procesada `weatherAUS_sumativa1_variables_clave.csv`, tablas, figuras, inventario de salidas e informe técnico.

### Semana 2 - Sumativa 2

La carpeta `semana2/` contiene la validación computacional de los resultados de Semana 1. El trabajo incorpora bootstrap percentil y BCa, prueba de permutación para la diferencia de medias de `Humidity3pm`, estabilidad de correlaciones, simulación Monte Carlo y análisis de robustez frente a valores extremos y supuestos estadísticos.

Productos principales de Semana 2:

```text
semana2/
├── data/
│   ├── input/
│   │   └── weatherAUS_sumativa1_variables_clave.csv
│   └── processed/
│       ├── weatherAUS_sumativa2_base_validacion.csv
│       └── resultados_validados_sumativa2.csv
├── docs/
│   ├── informe_sumativa2_rain_australia_g6.docx
│   ├── informe_sumativa2_rain_australia_g6.pdf
│   ├── inventario_outputs_sumativa2.csv
│   ├── figures/
│   └── tables/
├── notebooks/
│   └── Sumativa2_Rain_Australia_G6.ipynb
└── src/
    └── remuestreo_utils.py
```

La carpeta `semana2/data/input/` almacena la base procesada heredada desde la Sumativa 1, utilizada como insumo controlado de la Sumativa 2. La carpeta `semana2/data/processed/` queda reservada para los archivos generados por la ejecución del notebook de Semana 2.

### Semana 3 - Sumativa 3

La carpeta `semana3/` queda disponible para el desarrollo de modelamiento predictivo integrado. Los insumos validados para esa etapa se encuentran en `semana2/data/processed/resultados_validados_sumativa2.csv`.

## Reproducibilidad

Para ejecutar el proyecto se recomienda crear un entorno virtual por carpeta semanal e instalar las dependencias correspondientes:

```bash
cd semana2
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name mcdi501-g6 --display-name "Python 3.12 - MCDI501 G6"
```

El notebook de Semana 2 está diseñado para ejecutarse desde la raíz del repositorio o desde la carpeta `semana2/notebooks/`. Al finalizar, el flujo actualiza el inventario de salidas y ejecuta un control de integridad de archivos esperados. La ruta de entrada principal es:

```text
semana2/data/input/weatherAUS_sumativa1_variables_clave.csv
```

## Resultados validados para modelamiento posterior

La Sumativa 2 confirma que `Humidity3pm` presenta una diferencia robusta entre los grupos `RainTomorrow = Yes` y `RainTomorrow = No`. Además, las correlaciones de `Humidity3pm`, `RainToday_bin`, `Rainfall`, `Pressure3pm` y `MaxTemp` con `RainTomorrow_bin` mantienen dirección estable bajo remuestreo. Estos resultados fundamentan la selección inicial de variables candidatas para la etapa predictiva de Semana 3.
