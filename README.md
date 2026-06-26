# MCDIA500 - Estadística Computacional

## Descripción del proyecto

Para el proyecto escogimos el data set "<strong>Rain in Australia</strong>", el que Contiene aproximadamente 10 años de observaciones meteorológicas diarias de numerosas esta
ciones climáticas en Australia. 

El objetivo  bjetivo es predecir si lloverá al día siguiente basándose en las observaciones del día actual.

El proyecto está organizado para facilitar la trazabilidad, reutilización de funciones, ejecución en notebooks de Jupyter y control de versiones mediante GitHub.

---

## Estructura del proyecto
Para completar el curso de Estadística computacional cada carpeta semana<strong>*</strong> tiene el avance semanal (incremental) del proyecto.

```text

mcdia500-programacion-cd-g6/
│
├── semana1/
│
├── semana2/
│
├── semana3/
│
├── README.md
└── Changelog.md
```

### Descripción de carpetas y archivos

Cada carpeta semana1/semana2/semana3/ replica la siguiente estructura

- `data/raw/`: contiene los datos originales o crudos del proyecto.
- `data/processed/`: contiene datasets procesados, limpios o transformados.
- `docs/`: contiene documentación complementaria del proyecto.
- `notebooks/`: contiene los notebooks de análisis, limpieza, experimentación y modelamiento.
- `reports/`: contiene reportes, resultados, gráficos exportados o conclusiones generadas.
- `src/`: contiene funciones reutilizables, módulos auxiliares y código Python del proyecto.
---

## Requisitos previos

Antes de ejecutar el proyecto, es necesario tener instalado:

- Python 3.12.x
- Git
- Visual Studio Code, JupyterLab o Jupyter Notebook

---

## Instalación del proyecto

### 1. Clonar el repositorio

```powershell
git clone https://github.com/MagUnab/mcdia500-programacion-cd-g6.git
```

Ingresar a la carpeta donde se clonó el repositorio:</br>

NOTA: Para revisar el avance semanal debes ingresar a la carpeta correcta, según se indica a continuación:</br>

- Para Formativa 1. Informe 1 y Sumativa 1. Informe técnico de avance del proyecto -> semana1
- Para Sumativa 2. Informe 3 -> semana2
- Para Formativa 2. Informe 4 y Sumativa 3. Cierre y comunicación del proyecto-> semana3


```powershell
cd mcdia500-programacion-cd-g6/semana1
cd mcdia500-programacion-cd-g6/semana2
cd mcdia500-programacion-cd-g6/semana3
```
---

### 2. Crear el entorno virtual

```powershell
python -m venv .venv
```

---

### 3. Activar el entorno virtual

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Si la activación fue correcta, se debe ver algo como esto:

```text
(.venv) PS C:\ruta\del\proyecto\semana1 o semana2 o semana3 > -- según corresponda
```

---

### 4. Actualizar pip

```powershell
python -m pip install --upgrade pip
```

---

### 5. Instalar las dependencias del proyecto

```powershell
python -m pip install -r requirements.txt
```

---

### 6. Registrar el entorno virtual como kernel de Jupyter

```powershell
python -m ipykernel install --user --name mcdia500-g6 --display-name "Python 3.12 - MCDIA500 G6 Est Comp"
```

---

### 7. Ejecutar JupyterLab

```powershell
python -m jupyterlab --ServerApp.use_redirect_file=False
```

Dentro de JupyterLab seleccionarel kernel:

```text
Kernel → Change Kernel → Python 3.12 - MCDIA500 G6
```

---

## Uso del proyecto

Los notebooks del proyecto se encuentran en la carpeta:

```text
notebooks/
```

Los datos originales (crudos) se encuentran en:

```text
data/raw/
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

df = pd.read_csv("../data/raw/weatherAUS.csv", sep=";")
df.head()
```

---

## Control de versiones

Para revisar el estado del repositorio:

```powershell
git status
```

Para agregar cambios:

```powershell
git add .
```

Para crear un commit:

```powershell
git commit -m "feat: Nueva función python que realiza limpieza de dataset "
```

Para subir los cambios a GitHub:

```powershell
git push
```

---

## Archivos que no deben subirse al repositorio

La carpeta `.venv/` no debe subirse a GitHub, ya que cada persona que quiera clonar y trabajar en este proyecto debe crear su propio entorno virtual local a partir del archivo `requirements.txt`.

El archivo `.gitignore` debería considerar al menos:

```gitignore
.venv/
__pycache__/
.ipynb_checkpoints/
*.pyc
.env
```

---

## Reproducibilidad

Para reproducir el proyecto en otro equipo, por ejemplo la Fase 1 se deben ejecutar los siguientes pasos, 

```powershell
git clone https://github.com/MagUnab/mcdia500-programacion-cd-g6.git
cd mcdia500-programacion-cd-g6/semana1
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name mcdia500-g6 --display-name "Python 3.12 - MCDIA500 G6 Est Comp"
python -m jupyterlab --ServerApp.use_redirect_file=False
```

Con estos pasos, el entorno queda configurado para ejecutar los notebooks del proyecto.