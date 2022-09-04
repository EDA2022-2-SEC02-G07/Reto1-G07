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
