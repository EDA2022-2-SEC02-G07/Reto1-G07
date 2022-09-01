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
    catalog = {'amazon_prime': None,
               'netflix': None,
               'disney_plus': None,
               'hulu': None}

    catalog['amazon_prime'] = lt.newList('DOUBLE_LINKED')
    catalog['netflix'] = lt.newList('DOUBLE_LINKED')
    catalog['disney_plus'] = lt.newList('DOUBLE_LINKED')
    catalog['hulu'] = lt.newList('DOUBLE_LINKED')

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
    return lt.subList(streaming_list,0,3)

def lastThree(catalog,streamingService):
    streaming_list = catalog[streamingService]
    return lt.subList(streaming_list,(lt.size(streaming_list)-2),3)

# 1.1 Amazon Prime
def addContentAmazonPrime(catalog, content):
    amazon = catalog['amazon_prime']
    lt.addLast(amazon, content)
    return catalog

def amazonPrimeSize(catalog):
    return lt.size(catalog['amazon_prime'])

def firstThreeAmazonPrime(catalog):
    firstThree = ()

    i = 0
    node = catalog['amazon_prime']['first']
    while i < 3:
        
        contentTitle = node['info']['title']
        releaseDate = node['info']['release_year']
        duration = node['info']['duration']
        rating = node['info']['rating']

        firstThree += ([contentTitle, releaseDate, duration, rating],)

        node = node['next']
        i += 1

    return firstThree

def lastThreeAmazonPrime(catalog):
    lastThree = ()
    
    i = 0
    node = catalog['amazon_prime']['last']
    while i < 3:
        
        contentTitle = node['info']['title']
        releaseDate = node['info']['release_year']
        duration = node['info']['duration']
        rating = node['info']['rating']

        lastThree = ([contentTitle, releaseDate, duration, rating],) + lastThree

        node = node['prev']
        i += 1

    return lastThree


# 1.2 Disney Plus
def addContentDisneyPlus(catalog, content):
    amazon = catalog['disney_plus']
    lt.addLast(amazon, content)
    return catalog

def disneyPlusSize(catalog):
    return lt.size(catalog['disney_plus'])

def firstThreeDisneyPlus(catalog):
    firstThree = ()
    i = 0
    node = catalog['disney_plus']['first']
    while i < 3:
        
        contentTitle = node['info']['title']
        releaseDate = node['info']['release_year']
        duration = node['info']['duration']
        rating = node['info']['rating']

        firstThree += ([contentTitle, releaseDate, duration, rating],)

        node = node['next']
        i += 1

    #print(firstThree)
    return firstThree

def lastThreeDisneyPlus(catalog):
    lastThree = ()
    i = 0
    node = catalog['disney_plus']['last']
    while i < 3:
        
        contentTitle = node['info']['title']
        releaseDate = node['info']['release_year']
        duration = node['info']['duration']
        rating = node['info']['rating']

        lastThree = ([contentTitle, releaseDate, duration, rating],) + lastThree

        node = node['prev']
        i += 1

    return lastThree


# 1.3 Hulu
def addContentHulu(catalog, content):
    amazon = catalog['hulu']
    lt.addLast(amazon, content)
    return catalog

def huluSize(catalog):
    return lt.size(catalog['hulu'])

def firstThreeHulu(catalog):
    firstThree = ()
    i = 0
    node = catalog['hulu']['first']
    while i < 3:
        
        contentTitle = node['info']['title']
        releaseDate = node['info']['release_year']
        duration = node['info']['duration']
        rating = node['info']['rating']

        firstThree += ([contentTitle, releaseDate, duration, rating],)

        node = node['next']
        i += 1

    #print(firstThree)
    return firstThree

def lastThreeHulu(catalog):
    lastThree = ()
    i = 0
    node = catalog['hulu']['last']
    while i < 3:
        
        contentTitle = node['info']['title']
        releaseDate = node['info']['release_year']
        duration = node['info']['duration']
        rating = node['info']['rating']

        lastThree = ([contentTitle, releaseDate, duration, rating],) + lastThree

        node = node['prev']
        i += 1

    return lastThree


# 1.4 Netflix
def addContentNetflix(catalog, content):
    amazon = catalog['netflix']
    lt.addLast(amazon, content)
    return catalog

def netflixSize(catalog):
    return lt.size(catalog['netflix'])

def firstThreeNetflix(catalog):
    firstThree = ()
    i = 0
    node = catalog['netflix']['first']
    while i < 3:
        
        contentTitle = node['info']['title']
        releaseDate = node['info']['release_year']
        duration = node['info']['duration']
        rating = node['info']['rating']

        firstThree += ([contentTitle, releaseDate, duration, rating],)

        node = node['next']
        i += 1

    #print(firstThree)
    return firstThree

def lastThreeNetflix(catalog):
    lastThree = ()
    i = 0
    node = catalog['netflix']['last']
    while i < 3:
        
        contentTitle = node['info']['title']
        releaseDate = node['info']['release_year']
        duration = node['info']['duration']
        rating = node['info']['rating']

        lastThree = ([contentTitle, releaseDate, duration, rating],) + lastThree

        node = node['prev']
        i += 1

    return lastThree

