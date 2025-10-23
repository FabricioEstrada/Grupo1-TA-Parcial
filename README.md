# Repositorio de Avances en Predicción de Cintilación Ionosférica

Este repositorio contiene avances realizados para verificar que los datos proporcionados por el LISN del IGP cuenten con la información necesaria para nuestros modelos de predicción de cintilación ionosférica (índice S4).  

Se ha verificado cómo varía el índice S4 en diferentes años y meses con el fin de analizar su comportamiento y su impacto en señales GNSS.  

## Datos

- **JM91J_2025230.SAO**: Archivo obtenido desde la sección de ionosonde del LISN. Este archivo no está en texto plano, por lo que se está desarrollando un script para leerlo correctamente y extraer variables ionosféricas, especialmente de la capa F2, con el objetivo de medir la altura de la capa y predecir eventos de cintilación.  
- **CSV de GNSS (Jicamarca_S4_*.csv)**: Estos archivos exportados desde GNSS de LISN ya se encuentran en el formato adecuado para lectura con pandas. Se realizó un procesamiento previo de cada dataset obtenido de la página debido a que los datos estaban desordenados y no tenían etiquetas claras para cada variable.

## Cuadernos y Scripts

- **proyecto.ipynb**: Cuaderno principal con análisis y visualización de los datos S4.  
- **sao_parser.py**: Script en desarrollo para el manejo y lectura de datasets.  

## Estructura de Carpetas y Archivos

- `20XX_Mes/` : Carpeta que contiene los archivos crudos sin procesar de la página LISN. 
- `recursos/` : Recursos auxiliares.
- `Jicamarca_S4_MES20XX` : Archivos CSV procesados con la estructura correcta y legible.

## Estado Actual

- Se han integrado los archivos CSV grandes con Git LFS para permitir su manejo sin problemas de tamaño en GitHub.  
- Actualmente se está trabajando en agregar variables ionosféricas del archivo SAO y scripts para su correcta lectura.  

---

Este repositorio es un trabajo en progreso enfocado en análisis de datos ionosféricos para la predicción de cintilación, utilizando datasets de GNSS y datos de ionosonde.
