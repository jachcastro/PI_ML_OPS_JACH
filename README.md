![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

# PROYECTO INDIVIDUAL Nº1 
# Machine Learning Operations (MLOps) 

- Introducción. 
- Transformaciones. 
- Desarrollo API. 
- Análisis exploratorio de los datos. 
- Sistema de recomendación. 
- Enlaces. 
- Referencias. 

## Introducción 
El ciclo de vida de un proyecto de Machine Learning debe contemplar desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.

## Transformaciones
En el archivo ETL se hicieron las tranformaciones solicitadas
Conforme se iban trabajando los archivos se creo una carpeta para usarlo como fuente de datos
1_datasets_origen, como nos entregaron los archivos
2_datasets_etl, los csv después de las primeras transformaciones solicitadas
3_datasets_api, adapte los CSV para las funciones
4_datasets_eda, el resultado después de aplicar EDA
5_datasets_ml csv necesario para hacer la recomendación
Los campos compuestos por listas y diccionarios se separaron y se crearon nuevos archivos CSV, conforme se vaya reduciendo

## Desarrollo API. 
Localmente logramos hacer funcionar con FastApi
Luego lo publicamos en render

## Análisis exploratorio de los datos. 
Se analizaons los campos para decidir cual es relevante para el desarrollo a realizar
Para hacer una consulta de recomendacoón nos basaremos en dos formas
- en base al genero y popularidad 
- en base al titulo y contenido
obtendremos los datasets necesarios para ser consumidos por el modelo resultante 

## Sistema de recomendación
Se implementan dos modelos
y para el API quedaría

## Enlaces
- API
    https://pi-ml-ops-na32.onrender.com/
- Video
- Repositorio
- Datasets 

## Referencias
Enlces de todo lo consultado
