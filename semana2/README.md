# Semana 2 - Sumativa 2

Esta carpeta contiene el desarrollo de la Evaluación Sumativa 2 del proyecto Rain in Australia. El trabajo valida los resultados inferenciales obtenidos en la Sumativa 1 mediante remuestreo bootstrap, intervalos percentil y BCa, prueba de permutación, estabilidad de correlaciones, simulación Monte Carlo y análisis de robustez.

## Estructura

```text
semana2/
├── data/
│   └── processed/
├── docs/
│   ├── figures/
│   └── tables/
├── notebooks/
│   └── Sumativa2_Rain_Australia_G6.ipynb
├── src/
│   └── remuestreo_utils.py
└── requirements.txt
```

## Insumo principal

El notebook utiliza como entrada la base procesada de la Sumativa 1:

```text
../semana1/data/processed/weatherAUS_sumativa1_variables_clave.csv
```

## Salidas principales

El proceso genera tablas, figuras e inventario de resultados en `docs/`, además del archivo `data/processed/resultados_validados_sumativa2.csv`, que resume los resultados validados para la Sumativa 3.


## Criterio metodológico sobre valores faltantes

La Sumativa 2 utiliza casos válidos por análisis. Los valores faltantes no se imputan antes del bootstrap, de la permutación ni de las correlaciones, porque la finalidad de esta fase es validar los estimadores observados de la Sumativa 1 mediante remuestreo y simulación. Cada procedimiento elimina únicamente los registros que no contienen las variables necesarias para la estadística correspondiente. La imputación queda reservada para la etapa de modelamiento predictivo de la Sumativa 3, donde deberá incorporarse dentro del flujo de entrenamiento y validación para evitar fuga de información.

## Ejecución del notebook

El notebook `semana2/notebooks/Sumativa2_Rain_Australia_G6.ipynb` se entrega sin salidas ejecutadas. Para generar los resultados, se debe abrir en Jupyter Notebook o JupyterLab y ejecutar las celdas en orden. El modo metodológico predeterminado es `MODO_EJECUCION = 'completo'`, con 10.000 remuestras bootstrap, 10.000 permutaciones y 100.000 iteraciones Monte Carlo.


## Control de integridad

Al finalizar la ejecución, el notebook valida la existencia de las salidas esperadas y genera `docs/tables/11_control_integridad_salidas_sumativa2.csv`. Si alguna tabla, figura, archivo procesado o informe no está disponible, la última celda detiene la ejecución con un error explícito para evitar entregar una carpeta incompleta.
