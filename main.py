from fastapi import FastAPI
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI(title = "PI ML OPS", 
              description = "Javier Castro Hermoza")

@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma:str):
    '''Ingresas el idioma, retornando la cantidad de peliculas producidas en el mismo'''
    # Se ingresa un idioma (como están escritos en el dataset, no hay que traducirlos!). Debe devolver la cantidad de películas producidas en ese idioma.
    # Ejemplo de retorno: X cantidad de películas fueron estrenadas en idioma

    # Validar si el parámetro es de tipo string
    if not isinstance(idioma, str):
        return "El parámetro 'idioma' debe ser un string."

    # Leer el archivo CSV
    df = pd.read_csv('3_datasets_api/spoken_data.csv')
    
    # Filtrar las películas que coincidan con el idioma
    peliculas_filtradas = df[df['iso_639_1'].str.lower() == idioma.lower()]
    
    # Obtener la cantidad de películas para ese idioma
    cantidad_peliculas = peliculas_filtradas['id_movie'].nunique()
    
    return  f"{cantidad_peliculas} numero de películas que fueron estrenadas en idioma: {idioma}"

@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula: str):
    '''Ingresas la pelicula, retornando la duracion y el año'''

    # Se ingresa una pelicula. Debe devolver la duracion y el año.
    # Ejemplo de retorno: X . Duración: x. Año: xx

    # Validar si el parámetro es de tipo string
    if not isinstance(pelicula, str):
        return "El parámetro 'pelicula' debe ser un string."

    # Leer el archivo CSV que contiene la información de las películas
    df = pd.read_csv('3_datasets_api/peliculas_duracion.csv')

    # Buscar la película específica por su título en la columna 'title'
    pelicula_encontrada = df[df['title'].str.lower() == pelicula.lower()]

    if len(pelicula_encontrada) == 0:
        return f"No se encontró la película: {pelicula}"

    # Obtener la duración y el año de la película
    duracion = pelicula_encontrada['runtime'].iloc[0]
    año = pelicula_encontrada['release_year'].iloc[0]

    return f"{pelicula}. Duración: {duracion} minutos. Año: {año}"

@app.get('/franquicia/{franquicia}')
def franquicia(Franquicia: str):
    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio'''
    # def franquicia( Franquicia: str ): 
    # Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
    # Ejemplo de retorno: La franquicia X posee X peliculas, una ganancia total de x y una ganancia promedio de xx

    # Validar si el parámetro es de tipo string
    if not isinstance(Franquicia, str):
        return "El parámetro 'franquicia' debe ser un string."

    # Leer los archivos CSV en DataFrames
    franquicia_df= pd.read_csv('3_datasets_api/franquicia.csv')
    
    # Filtrar las películas de la franquicia
    franquicia_df = franquicia_df[franquicia_df['name_collection'].str.lower() == Franquicia.lower()]
    
    # Obtener la cantidad de películas
    cantidad_peliculas = franquicia_df.shape[0]
    
    # Obtener la ganancia total
    ganancia_total = franquicia_df['revenue'].sum()/1000000
    
    # Obtener la ganancia promedio
    ganancia_promedio = franquicia_df['revenue'].mean()/1000000
    
    # Formatear el resultado como un mensaje de retorno
    resultado = f"La franquicia {Franquicia} posee {cantidad_peliculas} películas, con una ganancia total de {ganancia_total:,.0f} millones y una ganancia promedio de {ganancia_promedio:,.0f} millones por cada una."
    
    return resultado

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(Pais: str):
    '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo'''
    # def peliculas_pais( Pais: str ): 
    # Se ingresa un país (como están escritos en el dataset, no hay que traducirlos!), retornando la cantidad de peliculas producidas en el mismo.
    # Ejemplo de retorno: Se produjeron X películas en el país X

    # Validar si el parámetro es de tipo string
    if not isinstance(Pais, str):
        return "El parámetro 'Pais' debe ser un string."

    # Leer el archivo CSV de películas y países
    countries_df = pd.read_csv('3_datasets_api/countries_data.csv')

    # Filtrar las películas que coincidan con el país ingresado
    peliculas_filtradas = countries_df[countries_df['iso_3166_1'].str.lower() == Pais.lower()]

    # Contar la cantidad de películas producidas en el país
    cantidad_peliculas = peliculas_filtradas.shape[0]
    if cantidad_peliculas>0 :
        pais_peliculas_filtradas = peliculas_filtradas.groupby('name_countries').first().index[0]
    else:
        pais_peliculas_filtradas = ''

    return f"Se produjeron {cantidad_peliculas} películas en el país {pais_peliculas_filtradas}"


@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(Productora: str):
    '''Ingresas la productora, entregandote el revunue total y la cantidad de peliculas que realizo '''
    # def productoras_exitosas( Productora: str ): 
    # Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo.
    # Ejemplo de retorno: La productora X ha tenido un revenue de x

    # Validar si el parámetro es de tipo string
    if not isinstance(Productora, str):
        return "El parámetro 'Productora' debe ser un string."

    # Leer el archivo CSV de productora exitosa
    productoras_exitosas_df = pd.read_csv('3_datasets_api/productoras_exitosas.csv')

    # Filtrar las películas que coincidan con la productora ingresada
    productoras_exitosas_df = productoras_exitosas_df[productoras_exitosas_df['name_companies'].str.lower() == Productora.lower()]

    # Calcular el total de revenue y la cantidad de películas realizadas
    revenue_total = productoras_exitosas_df['revenue'].sum()/100000
    cantidad_peliculas = productoras_exitosas_df['id_movie'].nunique()

    return f"La productora {Productora} ha tenido un revenue total de {revenue_total:,.0f} millones y ha realizado {cantidad_peliculas} películas."

@app.get('/obtener_director/{nombre_director}')
def obtener_director(Nombre_Director: str):
    ''' Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma. En formato lista'''
    # def get_director( Nombre_Director ): 
    # Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    # Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, 
    # en formato lista.

    # Validar si el parámetro es de tipo string
    if not isinstance(Nombre_Director, str):
        return "El parámetro 'Nombre_Director' debe ser un string."

    # Leer el archivo CSV de productora exitosa
    director_movies_df = pd.read_csv('3_datasets_api/director_movies.csv')

    # Filtrar las películas dirigidas por el director especificado
    director_movies_df = director_movies_df[(director_movies_df['name_crew'].str.lower() == Nombre_Director.lower())]

    if director_movies_df.empty:
        return "El director no se encuentra en el dataset o no ha dirigido películas."

    # Calcular el éxito del director (promedio de votos de sus películas)
    exito_director = director_movies_df['revenue'].sum()
    # Formatear los valores numéricos
    exito_director = '{:,.0f}'.format(exito_director)

    # Crear una lista para almacenar la información de cada película
    peliculas_info = []

    # Iterar sobre las filas del DataFrame para obtener la información requerida
    for index, row in director_movies_df.iterrows():
        retorno_individual = '{:,.0f}'.format(row['revenue'])
        costo = '{:,.0f}'.format(row['budget'])
        ganancia = '{:,.0f}'.format(row['revenue'] - row['budget'])
        pelicula_info = {
            'nombre': row['title'],
            'fecha_lanzamiento': str(row['release_date']),
            'retorno_individual': retorno_individual,
            'costo': costo,
            'ganancia': ganancia 
        }
        peliculas_info.append(pelicula_info)

    return exito_director, peliculas_info

# ML
merged_df = pd.read_csv("5_datasets_ml/movies_dataset_cleaned_ml.csv")
# Seleccionar los primeros n registros
half_rows = int(len(merged_df) * 0.9)
merged_df = merged_df.head(half_rows)

# Crear una matriz TF-IDF para las descripciones de las películas
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(merged_df['title'])

# Calcular la similitud del coseno entre las descripciones
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

@app.get('/Recomendar_Pelicula/{titulopelicula}')
def Recomendar_Pelicula(TituloPelicula:str):
    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista'''
    if not isinstance(TituloPelicula, str):
        return "El parámetro 'TituloPelicula' debe ser un string."
    if merged_df[merged_df['title'].str.lower() == TituloPelicula.lower()].shape[0]  == 0:
        return [] 
    idx = merged_df[merged_df['title'].str.lower() == TituloPelicula.lower()].index[0]  # Obtener el índice de la película
    sim_scores = list(enumerate(cosine_sim[idx]))  # Obtener los puntajes de similitud
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)  # Ordenar por similitud
    sim_scores = sim_scores[1:6]  # Obtener las 05 películas más similares (excluyendo la misma película)
    movie_indices = [i[0] for i in sim_scores]  # Obtener los índices de las películas similares
    return merged_df['title'].iloc[movie_indices]  # Devolver los títulos de las películas similares
    