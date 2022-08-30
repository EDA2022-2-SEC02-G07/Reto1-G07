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

    catalog['amazon_prime'] = lt.newList('SINGLE_LINKED')
    catalog['netflix'] = lt.newList('SINGLE_LINKED')
    catalog['disney_plus'] = lt.newList('SINGLE_LINKED')
    catalog['hulu'] = lt.newList('SINGLE_LINKED')

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
    for i in range(0,2):
        firstThree += (catalog['amazon_prime'][i],)
    
    return firstThree

def lastThreeAmazonPrime(catalog):
    lastThree = ()
    for i in range(1,3):
        lastThree = (catalog['amazon_prime'][-i],) + lastThree
    
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
    for i in range(0,2):
        firstThree += (catalog['disney_plus'][i],)
    
    return firstThree

def lastThreeDisneyPlus(catalog):
    lastThree = ()
    for i in range(1,3):
        lastThree = (catalog['disney_plus'][-i],) + lastThree
    
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
    for i in range(0,2):
        firstThree += (catalog['hulu'][i],)
    
    return firstThree

def lastThreeHulu(catalog):
    lastThree = ()
    for i in range(1,3):
        lastThree = (catalog['hulu'][-i],) + lastThree
    
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
    for i in range(0,2):
        firstThree += (catalog['netflix'][i],)
    
    return firstThree

def lastThreeNetflix(catalog):
    lastThree = ()
    for i in range(1,3):
        lastThree = (catalog['netflix'][-i],) + lastThree
    
    return lastThree

