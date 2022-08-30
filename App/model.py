"""
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


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():

    catalog = {'title': None,
               'director': None,
               'cast':None,
               'type': None,
               "country": None,
               'listed_in':None,
               'streaming_service': None,
               'streaming_service-title':None,
               'date_added':None,
               'release_year':None}

    catalog['title'] = lt.newList('ARRAY_LIST')
    catalog['director'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction=comparedirectors)
    catalog['cast'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=comparetagnames)
    catalog['type'] = lt.newList('ARRAY_LIST')
    catalog['country'] = lt.newList('ARRAY_LIST')
    catalog['listed_in'] = lt.newList('ARRAY_LIST')
    catalog['streaming_service'] = lt.newList('ARRAY_LIST')
    catalog['streaming_service-title'] = lt.newList('ARRAY_LIST')
    catalog['date_added'] = lt.newList('ARRAY_LIST')
    catalog['relase_year'] = lt.newList('ARRAY_LIST')

    return catalog

# Funciones para agregar informacion al catalogo
def addTitle(catalog, title):
#####
    lt.addLast(catalog['title'], title)
    directors = title['director'].split(",")
    cast = title["cast".split(",")]
    countries = title["country"]
    for director in directors:
        addTitleDirector(catalog, director.strip(), title)
    for actor in cast:
        addTitleCast(catalog, actor.strip(), title)
    for country in countries:
        addTitleCountry(catalog,country.strip(),title)
    return catalog
def addTitleDirector(catalog, directorname, title):
    """

    """
    directors = catalog['director']
    posdirector = lt.isPresent(directors, directorname)
    if posdirector > 0:
        director = lt.getElement(directors, posdirector)
    else:
        director = newDirector(directorname)
        lt.addLast(directors, director)
    lt.addLast(director['titles'], title)
    return catalog

def addTitleCast(catalog, actorname, title):
    """

    """
    actors = catalog['cast']
    posactor = lt.isPresent(actors, actorname)
    if posactor > 0:
        actor = lt.getElement(actors, posactor)
    else:
        actor = newActor(actorname)
        lt.addLast(actors, actor)
    lt.addLast(actor['titles'], title)
    return catalog

def addTitleCountry(catalog, countryname, title):
    """

    """
    countries = catalog['country']
    poscountry = lt.isPresent(countries, countryname)
    if poscountry > 0:
        country = lt.getElement(countries, poscountry)
    else:
        country = newCountry(countryname)
        lt.addLast(countries, country)
    lt.addLast(country['titles'], title)
    return catalog
    
def addTag(catalog, tag):
    """
    Adiciona un tag a la lista de tags
    """
    t = newTag(tag['Listed_in'], tag['tag_id'])
    lt.addLast(catalog['tags'], t)
    return catalog


# Funciones para creacion de datos
def newDirector(name):
    """
    """
    director = {'name': "", "titles": None,  "average_rating": 0}
    director['name'] = name
    director['titles'] = lt.newList('ARRAY_LIST')
    return director
def newActor(name):
    """
    """
    actor = {'name': "", "titles": None,  "average_rating": 0}
    actor['name'] = name
    actor['titles'] = lt.newList('ARRAY_LIST')
    return actor
def newCountry(name):
    """
    """
    country = {'name': "", "titles": None,  "average_rating": 0}
    country['name'] = name
    country['titles'] = lt.newList('ARRAY_LIST')
    return country
# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def comparedirectors(directorname1, director):
    if directorname1.lower() == director['name'].lower():
        return 0
    elif directorname1.lower() > director['name'].lower():
        return 1
    return -1

# Funciones de ordenamiento