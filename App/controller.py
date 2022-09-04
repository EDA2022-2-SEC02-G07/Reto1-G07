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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def newController(ListType):
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog(ListType)
    return control


# Inicialización del Catálogo de contenido

def loadData(control):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    catalog = control['model']
    amazonPrimeContent = loadAmazonPrimeData(catalog)
    disneyPlusContent = loadDisneyPlusData(catalog)
    huluContent = loadHuluData(catalog)
    netflixContent = loadNetflixData(catalog)
    
    return amazonPrimeContent, disneyPlusContent, huluContent, netflixContent

# Funciones para la carga de datos
def loadAmazonPrimeData(catalog):
    contentfile = cf.data_dir + 'Streaming/amazon_prime_titles-utf8-small.csv'
    input_file = csv.DictReader(open(contentfile, encoding='utf-8'))
    for content in input_file:
        model.addContent(catalog, content,'amazon_prime')
    return model.StreamingSize(catalog,'amazon_prime'), model.firstThree(catalog,'amazon_prime'), model.lastThree(catalog,'amazon_prime')

def loadDisneyPlusData(catalog):
    contentfile = cf.data_dir + 'Streaming/disney_plus_titles-utf8-small.csv'
    input_file = csv.DictReader(open(contentfile, encoding='utf-8'))
    for content in input_file:
        model.addContent(catalog, content,'disney_plus')
    return model.StreamingSize(catalog,'disney_plus'), model.firstThree(catalog,'disney_plus'), model.lastThree(catalog,'disney_plus')

def loadHuluData(catalog):
    contentfile = cf.data_dir + 'Streaming/hulu_titles-utf8-small.csv'
    input_file = csv.DictReader(open(contentfile, encoding='utf-8'))
    for content in input_file:
        model.addContent(catalog, content,'hulu')
    return model.StreamingSize(catalog,'hulu'), model.firstThree(catalog,'hulu'), model.lastThree(catalog,'hulu')

def loadNetflixData(catalog):
    contentfile = cf.data_dir + 'Streaming/netflix_titles-utf8-small.csv'
    input_file = csv.DictReader(open(contentfile, encoding='utf-8'))
    for content in input_file:
        model.addContent(catalog, content,'netflix')
    return model.StreamingSize(catalog,'netflix'), model.firstThree(catalog,'netflix'), model.lastThree(catalog,'netflix')


# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
