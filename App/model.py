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
import time
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

def TitleByTime(catalog,firstDate,LastDate):

    amazon = catalog["amazon_prime"]
    netflix = catalog["netflix"] 
    disney = catalog["disney_plus"]
    hulu = catalog["hulu"]

    returnlist = lt.newList("DOUBLE_LINKED")

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

    return FirstAndLastTitleByTime(returnlist)

def TitleSimplify(title,service):
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
def DateCompare(date,firstDate,LastDate):
    date__ = time.strptime(date, "%Y-%m-%d")
    firstDate_ = time.strptime(firstDate, "%Y-%m-%d")
    LastDate_ = time.strptime(LastDate, "%Y-%m-%d")

    if date__ <= LastDate_ and date__ >= firstDate_:
        return True
    else:
        return False
def FirstAndLastTitleByTime(list):
    i = 0
    first = []
    last = []
    nodo1 = list["first"]
    nodo2 = list["last"]["prev"]["prev"]
    while i < 3:
        first.append(nodo1["info"])
        last.append(nodo2["info"])
        nodo1 = nodo1["next"]
        nodo2 = nodo2["next"]
        i += 1
    return lt.size(list),first,last
def comparedate(pelicula1, pelicula2):

    fecha1 = str(pelicula1["date_added"])
    fecha2 = str(pelicula2["date_added"])

    fechadatetime1 = time.strptime(fecha1, "%Y-%m-%d")
    fechadatetime2 = time.strptime(fecha2, "%Y-%m-%d")

    if fechadatetime1 > fechadatetime2:
        return True
    if fechadatetime1 == fechadatetime2:
        return False