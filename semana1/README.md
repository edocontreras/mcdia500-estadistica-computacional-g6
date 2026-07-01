# Semana 1 - Sumativa 1

## Análisis exploratorio e inferencial del dataset *Rain in Australia*

**Integrantes:** Eduardo Contreras; Gonzalo Bouldres; Luis Díaz Giral
**Docente:** Dr. Jean Paul Maidana González
**Curso:** MCDI501 - Estadística Computacional para la Toma de Decisiones

---

## Objetivo de la entrega

El objetivo de esta entrega es desarrollar un análisis estadístico inicial sobre observaciones meteorológicas diarias de Australia, utilizando el dataset **Rain in Australia**, con énfasis en la variable objetivo `RainTomorrow`, la cual indica si llueve o no al día siguiente.

El análisis considera una revisión exploratoria de la base de datos, auditoría de valores faltantes, clasificación de variables, estadística descriptiva, análisis gráfico, matriz de correlación, estimación de intervalos de confianza y aplicación de pruebas de hipótesis sobre variables meteorológicas relevantes.

En particular, se estudia la relación entre variables climáticas como humedad, temperatura, presión, viento y precipitación, con la ocurrencia de lluvia al día siguiente, buscando generar una primera interpretación estadística del fenómeno meteorológico analizado.

---

## Entregables

La estructura principal de la Semana 1 es la siguiente:

```text
semana1/
├── data/
│   ├── raw/
│   │   └── weatherAUS.csv
│   └── processed/
│       └── weatherAUS_sumativa1_variables_clave.csv
├── docs/
│   ├── informe_sumativa1_rain_australia_g6.docx
│   ├── informe_sumativa1_rain_australia_g6.pdf
│   ├── inventario_outputs_sumativa1.csv
│   ├── figures/
│   └── tables/
├── notebooks/
│   └── Sumativa1_Rain_Australia_G6.ipynb
├── src/
│   └── estadistica_utils.py
└── requirements.txt
```

---

## Salidas generadas

La carpeta `docs/` consolida los principales productos generados durante la ejecución del notebook, considerando:

* 19 tablas en formato `.csv`, almacenadas en `docs/tables/`.
* 9 figuras en formato `.png`, almacenadas en `docs/figures/`.
* 1 inventario de salidas, disponible en `docs/inventario_outputs_sumativa1.csv`.
* 1 informe técnico en formato `.docx`, ubicado en `docs/informe_sumativa1_rain_australia_g6.docx`.
* 1 informe técnico en formato `.pdf`, ubicado en `docs/informe_sumativa1_rain_australia_g6.pdf`, en caso de ser requerido para la entrega formal.

---

## Alcance estadístico

La entrega desarrolla los siguientes componentes:

1. Descripción general del dataset `weatherAUS`.
2. Identificación y análisis de la variable objetivo `RainTomorrow`.
3. Auditoría de datos faltantes.
4. Segmentación de variables según tipo y relevancia analítica.
5. Estadística descriptiva de variables meteorológicas clave.
6. Construcción de variables binarias para lluvia observada y lluvia al día siguiente.
7. Construcción de variables temporales a partir de la fecha.
8. Matriz de correlación de Pearson entre variables numéricas seleccionadas.
9. Visualización exploratoria mediante histogramas, boxplots y gráficos de barras.
10. Estimación puntual e intervalos de confianza.
11. Prueba de hipótesis principal mediante t de Welch.
12. Prueba chi-cuadrado complementaria para variables categóricas.
13. Estimación de probabilidades condicionales asociadas a lluvia observada y lluvia al día siguiente.
14. Interpretación preliminar de resultados, alcances y limitaciones del análisis.

---

## Hipótesis estadística principal

La hipótesis principal del análisis se enfoca en evaluar si la humedad relativa observada durante la tarde se asocia con una mayor probabilidad de lluvia al día siguiente.

Se considera la variable `Humidity3pm`, comparando sus valores medios entre los días en que `RainTomorrow = Yes` y los días en que `RainTomorrow = No`.

La hipótesis se plantea de la siguiente manera:

```text
H0: La media de Humidity3pm es igual en los días con lluvia y sin lluvia al día siguiente.
H1: La media de Humidity3pm es mayor en los días con lluvia al día siguiente.
```

Para contrastar esta hipótesis se utiliza una prueba t de Welch, debido a que permite comparar dos grupos independientes sin asumir igualdad de varianzas.

---

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
notebooks/Sumativa1_Rain_Australia_G6.ipynb
```

---

## Reproducibilidad

Para mantener la reproducibilidad del análisis, el archivo original `weatherAUS.csv` debe permanecer en la siguiente ruta:

```text
semana1/data/raw/weatherAUS.csv
```

Al ejecutar el notebook completo, se actualizan automáticamente las salidas procesadas en las siguientes carpetas:

```text
semana1/data/processed/
semana1/docs/tables/
semana1/docs/figures/
```

El archivo `inventario_outputs_sumativa1.csv` resume las tablas y figuras generadas durante el análisis, permitiendo verificar la trazabilidad de los productos exportados.

---

## Consideraciones metodológicas

El análisis conserva los valores faltantes en la base original y trabaja con observaciones válidas según cada procedimiento estadístico. Esta decisión permite evitar imputaciones prematuras en una etapa exploratoria inicial y mantiene la trazabilidad del tratamiento de datos.

Las pruebas inferenciales se aplican sobre subconjuntos válidos de datos, considerando la disponibilidad efectiva de información para cada variable analizada. Por esta razón, el tamaño muestral puede variar entre análisis descriptivos, gráficos, correlacionales e inferenciales.

---

## Limitaciones del análisis

Los resultados corresponden a una primera etapa exploratoria e inferencial. Por lo tanto, no deben interpretarse como un modelo predictivo final de lluvia, sino como una aproximación estadística inicial para identificar relaciones relevantes entre variables meteorológicas.

Entre las principales limitaciones se consideran:

* Presencia de valores faltantes en distintas variables del dataset.
* Diferencias en el tamaño muestral efectivo según el análisis realizado.
* Uso de relaciones bivariadas y correlacionales en esta primera etapa.
* Ausencia de modelos predictivos multivariados en la Semana 1.
* Posible variabilidad climática entre localidades no modelada en profundidad en esta etapa.

---

## Conclusión general

La Semana 1 permite establecer una base estadística inicial para el análisis del dataset **Rain in Australia**. Los resultados muestran que variables como la humedad relativa a las 15:00, la ocurrencia de lluvia en el día actual y otras variables meteorológicas presentan asociaciones relevantes con la ocurrencia de lluvia al día siguiente.

En particular, la variable `Humidity3pm` muestra diferencias importantes entre los grupos definidos por `RainTomorrow`, lo que justifica su análisis como una variable relevante para etapas posteriores del proyecto.

Este trabajo deja preparada una base ordenada, reproducible y trazable para avanzar en futuras fases de análisis estadístico, modelamiento predictivo y toma de decisiones basada en datos.
