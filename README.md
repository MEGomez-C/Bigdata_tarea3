# Bigdata_tarea3
# Análisis Exploratorio de Datos de Netflix con PySpark (Procesamiento en Batch)

## 📌 Descripción del Proyecto
Este repositorio contiene la solución práctica para el procesamiento en batch utilizando **Apache Spark (PySpark)** como parte de la **Tarea 3: Procesamiento de Datos con Apache Spark** del curso de **Big Data** en la UNAD.

El objetivo principal es realizar un Análisis Exploratorio de Datos (EDA) sobre el catálogo de películas y series de **Netflix**, aplicando transformaciones, limpiezas y agregaciones distribuidas con PySpark DataFrames.

---

## 📁 Estructura del Repositorio
* `netflix_batch_analysis.py`: Script principal de Python/PySpark que ejecuta el pipeline de procesamiento eインExploratorio.
* `netflix_titles.csv`: Dataset obtenido de Kaggle con información detallada de más de 8,800 títulos de Netflix.
* `README.md`: Documentación e instrucciones de ejecución del proyecto.
* `LICENSE`: Licencia del repositorio.

---

## 📊 Preguntas de Negocio e Indicadores Analizados
El script `netflix_batch_analysis.py` responde a las siguientes interrogantes clave:
1. **Distribución por Tipo de Contenido:** Proporción total de Películas (*Movies*) vs. Series de Televisión (*TV Shows*).
2. **Top Países Productores:** Países con mayor volumen de títulos creados en la plataforma.
3. **Lanzamientos Recientes por Año:** Evolución del volumen de contenido añadido desde el año 2010.
4. **Clasificación por Edades (*Rating*):** Distribución del contenido según el público objetivo (ej. TV-MA, TV-14, R).

---

## 🛠️ Requisitos Previos e Instalación

### Requisitos del Sistema
* Java OpenJDK 11
* Python 3.8+
* Apache Spark 3.x / PySpark

### Instalación de Dependencias
Asegúrate de contar con `pyspark` instalado en tu entorno de trabajo:
```bash
pip install pyspark
