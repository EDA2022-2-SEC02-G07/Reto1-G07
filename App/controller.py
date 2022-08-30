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

def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog()
    return control


# Inicialización del Catálogo de libros

# Funciones para la carga de datos
def loadAmazonPrimeData(catalog):
    contentfile = cf.data_dir + 'Streaming/amazon_prime_titles-utf8-small.csv'
    input_file = csv.DictReader(open(contentfile, encoding='utf-8'))
    for content in input_file:
        model.addContentAmazonPrime(catalog, content)
    return model.amazonPrimeSize(catalog), model.firstThreeAmazonPrime(catalog), model.lastThreeAmazonPrime(catalog)

def loadDisneyPlusData(catalog):
    contentfile = cf.data_dir + 'Streaming/disney_plus_titles-utf8-small.csv'
    input_file = csv.DictReader(open(contentfile, encoding='utf-8'))
    for content in input_file:
        model.addContentDisneyPlus(catalog, content)
    return model.disneyPlusSize(catalog), model.firstThreeDisneyPlus(catalog), model.lastThreeDisneyPlus(catalog)

def loadHuluData(catalog):
    contentfile = cf.data_dir + 'Streaming/hulu_titles-utf8-small.csv'
    input_file = csv.DictReader(open(contentfile, encoding='utf-8'))
    for content in input_file:
        model.addContentHulu(catalog, content)
    return model.huluSize(catalog), model.firstThreeHulu(catalog), model.lastThreeHulu(catalog)

def loadNetflixData(catalog):
    contentfile = cf.data_dir + 'Streaming/netflix_titles-utf8-small.csv'
    input_file = csv.DictReader(open(contentfile, encoding='utf-8'))
    for content in input_file:
        model.addContentNetflix(catalog, content)
    return model.netflixSize(catalog), model.firstThreeNetflix(catalog), model.lastThreeNetflix(catalog)


# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
