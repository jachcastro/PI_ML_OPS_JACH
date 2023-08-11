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

Conforme se iban trabajando los archivos se creó una carpeta para usarlo como fuente de datos

- 1_datasets_origen, como nos entregaron los archivos
- 2_datasets_etl, los csv después de las primeras transformaciones solicitadas
- 3_datasets_api, adapte los CSV para las funciones
- 4_datasets_eda, el resultado después de aplicar EDA
- 5_datasets_ml csv necesario para hacer la recomendación

Los campos compuestos por listas y diccionarios se separaron y se crearon nuevos archivos CSV, conforme se vaya reduciendo

## Desarrollo API. 
Localmente logramos hacer funcionar con FastApi
Luego lo publicamos en render

## Análisis exploratorio de los datos. 
En esta etapa se decidió cual campo es relevante para el desarrollo a realizar
Para hacer una consulta de recomendación de película nos basaremos en género, ranking, director, título y contenido y obtuvimos los datasets necesarios para ser consumidos por el modelo que vayamos a usar en el Machine Learning 

Se analizaron los campos por separado:

- Numérico
- Categórico
- Fecha

Los datasets trabajados fueron los obtenidos luego del ETL, en el drive los encontrarán en la carpeta 2_datasets_etl

-	movies_dataset_cleaned.csv, las películas 
-	cast_data.csv, casting 
-	collection_data.csv, Saga
-	companies_data.csv, compañías 
-	countries_data.csv, países 
-	crew_data.csv, directores 
-	genres_data.csv, géneros de las películas 
-	spoken_data.csv

Se analizo todos los campos de todos los CSV 

* Del dataset de movies
    * De las variables numéricas solo usaremos 'vote_average'
    * De las categóricas ['overview', 'tagline', 'title']
    * También creamos y nos quedamos con release_month y release_year

* Del dataset de Cast
    * Ningún campo de este dataset se utilizara para recomendar una película 
    * 'character' y 'name_cast' es muy disperso y variable para recomendar una película
    * 'gender' no es determinante para recomendar una película 

* Del dataset de Collection 
    * name_collection para recomendar una película

* Del dataset de Companies
    * name_companies para recomendar una película

* Del dataset de Countries
    * name_countries para recomendar una película

* Del dataset de Crew
    * department, job y name_crew para recomendar una película

* Del dataset de Spoken
    * name_spoken para recomendar una película

* Del dataset de Genero
    * name_genres para recomendar una película

## Sistema de recomendación
Quise implementar un dataset con los siguientes campos:

-	idMovie
-	Title
-	Overview
-	Tagline 
-	Collection
-	vote_average
-	Director
-	Genero (vectorizado una columna por genero)
-	Release_Year
-	Release_Month

Luego juntar los campos Title + Overview + Tag Line para hacer una nube de palabras.

Limpiar este nuevo campo, quitando los caracteres especiales, todo en minúsculas, tokenizar y lematizar los verbos. Para obtener textos limpios para analizar. Este nuevo campo Overview_Clean nos iba a servir para entrenar el modelo


Pero las limitaciones de memoria hacen que se reduzca la forma de programar y solo nos limitamos al campo titulo:
-	En mi PC con 8 GB de RAM me dejo procesar hasta el 90% de los registros
-	En render con 512 MB de RAM solo me permitió cargar el 10% de los títulos 


TfidfVectorizer: se utiliza para convertir los títulos o descripciones de películas en representaciones numéricas (matrices TF-IDF).


cosine_similarity: se utiliza para calcular la similitud del coseno entre estas representaciones numéricas, lo que permite identificar qué películas son más similares en términos de su contenido textual.


Luego de crear las matrices con Overview_Clean al procedimiento era aplicar filtros
-	Encontrar películas de la misma colección
-	Encontrar películas de los mismos géneros
-	Encontrar películas del director
-	Ordenar por año, mes y vote_average  


Durante el despliegue del API
-	Fue muy práctico la implementación con FastAPI
-	Nunca me voy a olvidar de esta instrucción:
python -m uvicorn main:app –reload
-	Mientras uvicorn este activo en consola se graban las modificaciones y uvicorn refresca los cambios, me pareció muy útil y practico
-	Luego en Render, el despliegue no fue complicado 
-	Entender que hacia pip freeze > requirements.txt
-	Pelear con render hasta que suba y acepte el proyecto 
-	Pelear otro rato con el archivo requirements.txt hasta entender que debemos instalar las versiones que soporta render, y lo principal leer el mensaje de error y que te recomienda que versiones puede soportar 
-	Darte cuenta que es lo mismo colocar o no la versión en requirements.txt
    - uvicorn==0.22.0
    - scikit-learn
-	Fue muy gratificante encontrar el botón “Clear build cache & deploy”

## Enlaces

- API
    - https://pi-ml-ops-na32.onrender.com/docs 
- Video
    - https://drive.google.com/file/d/1vwk-0-a5L_9zWtxzQbM0VKPOhip1i5Aa/view?usp=sharing
- Repositorio
    - https://github.com/jachcastro/PI_ML_OPS_JACH/blob/main/README.md
- Carpeta compartida con Jupiter Notebooks, Datasets, video, main.py 
    - https://drive.google.com/drive/folders/1QqJKcEb8_8_VXuecfCz_ppcAxDxiuSc0?usp=sharing

## Referencias
Enlaces de todo lo consultado:
- https://www.youtube.com/watch?v=wBu0hQQVdcE
- https://www.youtube.com/watch?v=aatztrDAz4I
- https://www.aprendemachinelearning.com/sistemas-de-recomendacion/
- https://www.facebook.com/watch/live/?ref=watch_permalink&v=461797502778635
- https://www.kaggle.com/code/ryoaoki1/sistema-de-recomendaci-n-de-pel-culas/notebook

Escuchando todo a 2X, super concentrado, lo disfrute mucho.
