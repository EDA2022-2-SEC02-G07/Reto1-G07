﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import time
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(ListType):
    catalog = {'amazon_prime': None,
               'netflix': None,
               'disney_plus': None,
               'hulu': None}

    catalog['amazon_prime'] = lt.newList(ListType)
    catalog['netflix'] = lt.newList(ListType)
    catalog['disney_plus'] = lt.newList(ListType)
    catalog['hulu'] = lt.newList(ListType)

    return catalog

# Funciones para agregar informacion al catalogo
def addContent(catalog, content,streaming_platform):
    platform = catalog[streaming_platform]
    lt.addLast(platform, content)
    return catalog

def StreamingSize(catalog,streaming_platform):
    return lt.size(catalog[streaming_platform])

def firstThree(catalog,streamingService):
    streaming_list = catalog[streamingService] 
    sublist = lt.subList(streaming_list,0,3)
    tuple = ()
    for i in lt.iterator(sublist):
        dictt = {"title":i["title"], "release_year":i["release_year"],
        "duration":i["duration"],"listed_in":i["listed_in"]}
        tuple += (dictt,)
    return tuple
def lastThree(catalog,streamingService):
    streaming_list = catalog[streamingService]
    sublist = lt.subList(streaming_list,(lt.size(streaming_list)-2),3)
    tuple = ()
    for i in lt.iterator(sublist):
        dictt = {"title":i["title"], "release_year":i["release_year"],
        "duration":i["duration"],"listed_in":i["listed_in"]}
        tuple += (dictt,)
    return tuple

def sortbydate(catalog,algorithm):
    start_time = getTime()
    if algorithm == 0:
        sorted_catalog = {"amazon_prime":se.sort(catalog["amazon_prime"],cmpMoviesByReleaseYear),
            "netflix":se.sort(catalog["netflix"],cmpMoviesByReleaseYear),
            "disney_plus":se.sort(catalog["disney_plus"],cmpMoviesByReleaseYear),
            "hulu":se.sort(catalog["hulu"],cmpMoviesByReleaseYear)}
        end_time = getTime()
    elif algorithm == 1:
        sorted_catalog = {"amazon_prime":ins.sort(catalog["amazon_prime"],cmpMoviesByReleaseYear),
            "netflix":ins.sort(catalog["netflix"],cmpMoviesByReleaseYear),
            "disney_plus":ins.sort(catalog["disney_plus"],cmpMoviesByReleaseYear),
            "hulu":ins.sort(catalog["hulu"],cmpMoviesByReleaseYear)}
        end_time = getTime()
    elif algorithm == 2:
        sorted_catalog = {"amazon_prime":sa.sort(catalog["amazon_prime"],cmpMoviesByReleaseYear),
            "netflix":sa.sort(catalog["netflix"],cmpMoviesByReleaseYear),
            "disney_plus":sa.sort(catalog["disney_plus"],cmpMoviesByReleaseYear),
            "hulu":sa.sort(catalog["hulu"],cmpMoviesByReleaseYear)}
        end_time = getTime()
    return sorted_catalog,deltaTime(start_time,end_time)
def cmpMoviesByReleaseYear(movie1, movie2):
    """
    Devuelve verdadero (True) si el release_year de movie1 son menores que los
    de movie2, en caso de que sean iguales tenga en cuenta el titulo y en caso de que
    ambos criterios sean iguales tenga en cuenta la duración, de lo contrario devuelva
    falso (False).
    Args:
    movie1: informacion de la primera pelicula que incluye sus valores 'release_year',
    ‘title’ y ‘duration’
    movie2: informacion de la segunda pelicula que incluye su valor 'release_year', 
    ‘title’ y ‘duration’
    """
    if movie1["release_year"] < movie2["release_year"]:
        return True
    if movie1["release_year"] == movie2["release_year"]:
        if movie1["title"] < movie2["title"]:
            return True
        elif movie1["title"] == movie2["title"]:
            if movie1["duration"] < movie2["duration"]:
                return True
    else:
        return False

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)
def deltaTime(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
def TitleByTime(catalog,firstDate,LastDate): #Función Principal Requerimiento 2

    amazon = catalog["amazon_prime"]
    netflix = catalog["netflix"] 
    disney = catalog["disney_plus"]
    hulu = catalog["hulu"]

    returnlist = lt.newList()

    for title in lt.iterator(amazon):
        date = title["date_added"]
        if date != '' and title["type"] == "TV Show":
            if DateCompare(date,firstDate,LastDate) == True:
                lt.addLast(returnlist,TitleSimplify(title,"Amazon Prime"))
    for title in lt.iterator(netflix):
        date = title["date_added"]
        if date != '' and title["type"] == "TV Show":
            if DateCompare(date,firstDate,LastDate) == True:
                lt.addLast(returnlist,TitleSimplify(title,"Netflix"))
    for title in lt.iterator(disney):
        date = title["date_added"]
        if date != '' and title["type"] == "TV Show":
            if DateCompare(date,firstDate,LastDate) == True:
                lt.addLast(returnlist,TitleSimplify(title,"Disney Plus"))
    for title in lt.iterator(hulu):
        date = title["date_added"]
        if date != '' and title["type"] == "TV Show":
            if DateCompare(date,firstDate,LastDate) == True:
                lt.addLast(returnlist,TitleSimplify(title,"Hulu"))

    sa.sort(returnlist, comparedate)

    return lt.size(returnlist),returnlist
def TitleSimplify(title,service): #Función Auxiliar Requerimiento 2
    simplify = {"type":title["type"],"date_added":title["date_added"],
        "title":title["title"],
        "duration":title["duration"],
        "date_added":title["date_added"],
        "streaming_service":service,
        "director":title["director"],
        "cast":title["cast"]}
    for key in simplify:
        if simplify[key] == '':
            simplify[key] = "Unkown"
    return simplify
def DateCompare(date,firstDate,LastDate): #Función Auxiliar Requerimiento 2
    date__ = time.strptime(date, "%Y-%m-%d")
    firstDate_ = time.strptime(firstDate, "%Y-%m-%d")
    LastDate_ = time.strptime(LastDate, "%Y-%m-%d")

    if date__ <= LastDate_ and date__ >= firstDate_:
        return True
    else:
        return False
def comparedate(pelicula1, pelicula2): #CMP Function para requerimiento 2

    fecha1 = str(pelicula1["date_added"])
    fecha2 = str(pelicula2["date_added"])

    fechadatetime1 = time.strptime(fecha1, "%Y-%m-%d")
    fechadatetime2 = time.strptime(fecha2, "%Y-%m-%d")

    if fechadatetime1 > fechadatetime2:
        return True
    if fechadatetime1 == fechadatetime2:
        return False
def TitlesByActor(actor,catalog): #Función Principal Requerimiento 3
    TV_count = 0
    Movie_count = 0
    titles = lt.newList()
    for i in lt.iterator(catalog["amazon_prime"]):
        if (i["cast"] != "") and (actor in i["cast"]):
            titles,TV_count,Movie_count = Add_Actor_title(i,titles,"amazon",TV_count,Movie_count)
    for i in lt.iterator(catalog["netflix"]):
        if (i["cast"] != "") and (actor in i["cast"]):
            titles,TV_count,Movie_count = Add_Actor_title(i,titles,"netflix",TV_count,Movie_count)
    for i in lt.iterator(catalog["disney_plus"]):
        if (i["cast"] != "") and (actor in i["cast"]):
            titles,TV_count,Movie_count = Add_Actor_title(i,titles,"disney_plus",TV_count,Movie_count)
    for i in lt.iterator(catalog["hulu"]):
        if (i["cast"] != "") and (actor in i["cast"]):
            titles,TV_count,Movie_count = Add_Actor_title(i,titles,"hulu",TV_count,Movie_count)
    titles1 = sa.sort(titles,ActorCompare)
    return titles1,TV_count,Movie_count
def Add_Actor_title(title,titles,stream,TV_count,Movie_count): #Función Auxiliar Requerimiento 3
    if title["type"] == "TV Show":
        TV_count += 1
    elif title["type"] == "Movie":
        Movie_count += 1
    lt.addLast(titles, {"type":title["type"],"title":title["title"],"release_year":title["release_year"],
        "director":title["director"],"streaming_platform":stream,"duration":title["duration"],
        "cast":title["cast"],"country":title["country"],"listed_in":title["listed_in"],"description":title["description"]})
    return titles,TV_count,Movie_count
def ActorCompare(title1,title2): #Función Auxiliar Requerimiento 3
    if title1["title"] < title2["title"]:
        return True
    elif title1["title"] == title2["title"]:
        if title1["release_year"] < title2["release_year"]:
            return True
        elif title1["release_year"] == title2["release_year"]:
            if title1["director"] < title2["director"]:
                return True
    else:
        return False