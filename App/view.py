"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def newController(ListType = "SINGLE_LINKED"):
    """
        Se crea una instancia del controlador
    """
    control = controller.newController(ListType)
    return control
def selector():
    ints = input("Ingrese el tipo de lista:\nLINKED_LIST:0\nARRAY_LIST:1\n")
    if ints == "0":
        control = newController()
    elif ints == "1":
        control = newController("ARRAY_LIST")
    else:
        control = None
    size = input("Ingrese el tamaño de la muestra:(-5pct,-10pct,-20pct,-30pct,-50pct,-80pct,-small,-large)\n")
    if size[0] != "-":
        size = None
    algorithm = input("Ingrese el algoritmo deseado:\nSelection:0\nInsertion:1\nShell:2\n")
    return control,size,int(algorithm)
def sortbydate(control,algorithm):
    sorted_catalog,deltatime = controller.sortbydate(control,algorithm)
    print("Tiempo de ejecución:",str(deltatime))
def loadData(control,size):
    Amazon,Disney,Hulu,Netflix = controller.loadData(control,size)

    return Amazon,Disney,Hulu,Netflix

def PrintStreamingData(Data):
    Amazon,Disney,Hulu,Netflix= Data
    
    size_Amazon, first_Amazon, last_Amazon = Amazon
    size_Disney, first_Disney, last_Disney = Disney
    size_Hulu, first_Hulu, last_Hulu = Hulu
    size_Netflix, first_Netflix, last_Netflix = Netflix  

    print("Total de Contenidos Amazon Prime Video: " + str(size_Amazon))
    print("Primeros 3 contenidos de Amazon:\n", str(first_Amazon))
    print("Ultimos 3 contenidos de Amazon:\n", str(last_Amazon))
    
    print("Total de Contenidos Disney Plus: " + str(size_Disney))
    print("Primeros 3 contenidos de Disney Plus:\n", str(first_Disney))
    print("Ultimos 3 contenidos de Disney Plus:\n", str(last_Disney))

    print("Total de Contenidos Hulu: " + str(size_Hulu))
    print("Primeros 3 contenidos de Hulu:\n", str(first_Hulu))
    print("Ultimos 3 contenidos de Hulu:\n", str(last_Hulu))

    print("Total de Contenidos Netflix: " + str(size_Netflix))
    print("Primeros 3 contenidos de Netflix:\n", str(first_Netflix))
    print("Primeros 3 contenidos de Netflix:\n", str(last_Netflix))

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Lista de las películas estrenadas en un periodo de tiempo")
    print("3- Lista de programas de televisión agregados en un periodo de tiempo")
    print("4- Encontrar contenido donde participa un acto")
    print("5- Encontrar contenido por un género especifico")
    print("6- Encontrar contenido producido por país")
    print("7- Encontrar contenido con un director involucrado")
    print("8- Listar el top de géneros con más contenido")
    print("9-  Listar el top de los actores con más participaciones en contenido")
    print("10- Definir lista,tamaño y algoritmo")
    print("11- Ordenar Listas por año de lanzamiento.")
    print("0- Salir")

control = None
size = "-small"
algorithm = 0
"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs) == 1:
        if control == None:
            control = newController()
        print("Cargando información de los archivos ....")
        Data = loadData(control,size)
        PrintStreamingData(Data)
    elif int(inputs) == 10:
        control,size,algorithm = selector()
    elif int(inputs) == 11:
        sortbydate(control,algorithm)
    elif int(inputs[0]) == 0:
        sys.exit(0)

    else:
        sys.exit(0)
sys.exit(0)
