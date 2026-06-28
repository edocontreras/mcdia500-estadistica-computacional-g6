# MCDI501 - Estadística Computacional para la Toma de Decisiones

## Descripción del proyecto

Para el proyecto se seleccionó el dataset **Rain in Australia**, el cual contiene aproximadamente 10 años de observaciones meteorológicas diarias registradas en distintas estaciones climáticas de Australia.

El objetivo del proyecto es analizar variables meteorológicas relevantes y estudiar su relación con la variable `RainTomorrow`, que indica si lloverá o no al día siguiente. A partir de este conjunto de datos, el repositorio organiza el desarrollo progresivo de análisis exploratorio, estadística descriptiva, inferencia estadística y posteriores etapas analíticas del proyecto.

El proyecto está organizado para facilitar la trazabilidad del trabajo, la reutilización de funciones, la ejecución de notebooks en Jupyter y el control de versiones mediante GitHub.

## Estructura del proyecto

Para completar el curso de Estadística Computacional, cada carpeta `semana*` contiene el avance semanal e incremental del proyecto.

```text
mcdia500-estadistica-computacional-g6/
│
├── semana1/
│   ├── data/
│   ├── docs/
│   ├── notebooks/
│   ├── src/
│   ├── README.md
│   ├── LICENSE
│   └── requirements.txt
│
├── semana2/
│
├── semana3/
│
├── README.md
├── CHANGELOG.md
└── .gitignore
```

## Descripción de carpetas y archivos

Cada carpeta semanal contiene una estructura orientada a mantener orden, reproducibilidad y trazabilidad del proyecto.

* `data/raw/`: contiene los datos originales o crudos del proyecto.
* `data/processed/`: contiene datasets procesados, limpios o transformados.
* `docs/`: contiene documentación complementaria del proyecto, informes, inventarios, tablas y figuras.
* `docs/figures/`: contiene gráficos y visualizaciones exportadas desde los notebooks.
* `docs/tables/`: contiene tablas de resultados generadas durante el análisis.
* `notebooks/`: contiene los notebooks de análisis, limpieza, experimentación y modelamiento.
* `src/`: contiene funciones reutilizables, módulos auxiliares y código Python del proyecto.
* `requirements.txt`: contiene las dependencias necesarias para ejecutar cada entrega.

## Avance por semana

La organización del repositorio considera las siguientes etapas:

* **Semana 1:** Formativa 1, Informe 1 y Sumativa 1. Incluye análisis exploratorio, estadística descriptiva, inferencia inicial, matriz de correlación, tablas, figuras, inventario de salidas y notebook reproducible.
* **Semana 2:** Sumativa 2, Informe 3. Carpeta reservada para el desarrollo de la siguiente etapa del proyecto.
* **Semana 3:** Formativa 2, Informe 4 y Sumativa 3. Carpeta reservada para el cierre, comunicación y consolidación final del proyecto.

## Estado de la Semana 1

La carpeta `semana1/` contiene actualmente los principales productos de la primera entrega:

```text
semana1/
├── data/
│   ├── raw/
│   │   └── weatherAUS.csv
│   └── processed/
│       └── weatherAUS_formativa1_variables_clave.csv
├── docs/
│   ├── figures/
│   ├── tables/
│   ├── inventario_outputs_formativa1.csv
│   └── informe_formativa1_rain_australia.pdf
├── notebooks/
│   └── Formativa1_Rain_Australia_G6.ipynb
├── src/
│   └── estadistica_utils.py
├── README.md
├── LICENSE
└── requirements.txt
```

La Semana 1 considera:

* 15 tablas en `docs/tables/`.
* 9 figuras en `docs/figures/`.
* 1 inventario de salidas en `docs/inventario_outputs_formativa1.csv`.
* 1 notebook principal en `notebooks/Formativa1_Rain_Australia_G6.ipynb`.
* 1 dataset procesado en `data/processed/`.
* 1 informe técnico en `docs/informe_formativa1_rain_australia.pdf`.

## Requisitos previos

Antes de ejecutar el proyecto, es necesario tener instalado:

* Python 3.12.x
* Git
* Visual Studio Code, JupyterLab o Jupyter Notebook

## Instalación del proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/edocontreras/mcdia500-estadistica-computacional-g6.git
```

Ingresar a la carpeta donde se clonó el repositorio:

```bash
cd mcdia500-estadistica-computacional-g6
```

Para revisar el avance semanal, se debe ingresar a la carpeta correspondiente. Por ejemplo, para Semana 1:

```bash
cd semana1
```

Para semanas posteriores, se debe volver a la raíz del repositorio e ingresar a la carpeta respectiva:

```bash
cd semana2
```

o:

```bash
cd semana3
```

### 2. Crear el entorno virtual

Desde la carpeta semanal correspondiente, ejecutar:

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual

En Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

Si la activación fue correcta, se debe observar una estructura similar a:

```text
(.venv) PS C:\ruta\del\proyecto\semana1>
```

### 4. Actualizar pip

```bash
python -m pip install --upgrade pip
```

### 5. Instalar las dependencias del proyecto

```bash
python -m pip install -r requirements.txt
```

### 6. Registrar el entorno virtual como kernel de Jupyter

```bash
python -m ipykernel install --user --name mcdi501-g6 --display-name "Python 3.12 - MCDI501 G6 Est Comp"
```

### 7. Ejecutar JupyterLab

```bash
python -m jupyterlab --ServerApp.use_redirect_file=False
```

Dentro de JupyterLab, seleccionar el kernel:

```text
Kernel → Change Kernel → Python 3.12 - MCDI501 G6 Est Comp
```

## Uso del proyecto

Los notebooks del proyecto se encuentran en la carpeta:

```text
notebooks/
```

Los datos originales o crudos se encuentran en:

```text
data/raw/
```

Los datasets procesados se encuentran en:

```text
data/processed/
```

Las funciones reutilizables se encuentran en:

```text
src/
```

Desde un notebook ubicado en la carpeta `notebooks/`, se pueden importar funciones desde `src/` usando:

```python
import sys
from pathlib import Path

project_root = Path.cwd().parent
sys.path.append(str(project_root / "src"))
```

Ejemplo de carga de datos:

```python
import pandas as pd

df = pd.read_csv("../data/raw/weatherAUS.csv")
df.head()
```

## Control de versiones

Para revisar el estado del repositorio:

```bash
git status
```

Para agregar cambios:

```bash
git add .
```

Para crear un commit:

```bash
git commit -m "docs: actualiza documentación del proyecto"
```

Para subir los cambios a GitHub:

```bash
git push
```

## Archivos que no deben subirse al repositorio

La carpeta `.venv/` no debe subirse a GitHub, ya que cada persona que clone y trabaje en este proyecto debe crear su propio entorno virtual local a partir del archivo `requirements.txt`.

El archivo `.gitignore` debería considerar al menos:

```text
.venv/
__pycache__/
.ipynb_checkpoints/
*.pyc
.env
```

## Reproducibilidad

Para reproducir el proyecto en otro equipo, por ejemplo la Semana 1, se deben ejecutar los siguientes pasos:

```bash
git clone https://github.com/edocontreras/mcdia500-estadistica-computacional-g6.git
cd mcdia500-estadistica-computacional-g6/semana1
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name mcdi501-g6 --display-name "Python 3.12 - MCDI501 G6 Est Comp"
python -m jupyterlab --ServerApp.use_redirect_file=False
```

Con estos pasos, el entorno queda configurado para ejecutar los notebooks del proyecto.

Para mantener la reproducibilidad del análisis de Semana 1, el archivo original debe permanecer en:

```text
semana1/data/raw/weatherAUS.csv
```

El notebook principal de Semana 1 es:

```text
semana1/notebooks/Formativa1_Rain_Australia_G6.ipynb
```

## Integrantes

* Eduardo Contreras
* Gonzalo Bouldres
* Luis Díaz Giral

## Docente

Dr. Jean Paul Maidana González

## Curso

MCDI501 - Estadística Computacional para la Toma de Decisiones
