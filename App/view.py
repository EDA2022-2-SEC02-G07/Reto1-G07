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
from prettytable import PrettyTable,ALL

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
        ints = "SINGLE_LINKED"
    elif ints == "1":
        control = newController("ARRAY_LIST")
        ints = "ARRAY_LIST"
    else:
        control = None
    size = input("Ingrese el tamaño de la muestra:(-5pct,-10pct,-20pct,-30pct,-50pct,-80pct,-small,-large)\n")
    if size[0] != "-":
        size = None
    algorithm = input("Ingrese el algoritmo deseado:\nSelection:0\nInsertion:1\nShell:2\nMerge:3\nQuick:4\n")
    return control,size,int(algorithm),ints
def sortbydate(control,algorithm,ListType):
    sorted_catalog,deltatime = controller.sortbydate(control,algorithm,ListType)
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
def printReq2(control,date1,date2):
    size,list = controller.TitleByTime(control,date1,date2)
    print("Hay "+ str(size)+" 'TV SHOW' entre "+date1 + " y " + date2+".")
    print("Los Primeros y Últimos 3 programas son:")
    tabla = PrettyTable()
    tabla.field_names = ["type", "date_Added", "title", "duration", "release_year", "stream_service", "director", "cast"]
    tabla._max_width = {"cast":25}
    tabla.hrules = ALL
    tabla.horizontal_char = "="
    if size >= 6:
        first3 = lt.subList(list, 1, 3)
        last3 = lt.subList(list, lt.size(list)-2, 3)
        for title in lt.iterator(first3):
            tabla.add_row([title["type"],title["date_added"],title["title"],title["duration"],title["date_added"],
            title["streaming_service"],title["director"],title["cast"]])
        for title in lt.iterator(last3):
            tabla.add_row([title["type"],title["date_added"],title["title"],title["duration"],title["date_added"],
            title["streaming_service"],title["director"],title["cast"]])
    else:
        for title in lt.iterator(list):
            tabla.add_row([title["type"],title["date_added"],title["title"],title["duration"],title["date_added"],
            title["streaming_service"],title["director"],title["cast"]])
    print(tabla)
def printReq3(control,actor):
    title, TV_count, Movie_count = controller.TitlesByActor(control,actor)
    tabla0 = PrettyTable()
    tabla0.field_names = ["type","count"]
    tabla0.add_row(["Movie",Movie_count])
    tabla0.add_row(["TV SHOW",TV_count])
    print(tabla0)
    tabla1 = PrettyTable()
    tabla1.field_names = ["type", "title", "release_year", "director", "stream_service", "duration", "cast", "country", "listed_in", "description"]
    tabla1._max_width = {"cast":15,"description":10}
    if lt.size(title) >= 6:
        first3 = lt.subList(title, 0, 3)
        last3 = lt.subList(title, lt.size(title)-2, 3)

        for title in lt.iterator(first3):
            tabla1.add_row([title["type"],title["title"],title["release_year"],title["director"],title["streaming_platform"],
                title["duration"],title["cast"], title["country"],title["listed_in"],title["description"][0:100]+"(...)"])

        for title in lt.iterator(last3):
            tabla1.add_row([title["type"],title["title"],title["release_year"],title["director"],title["streaming_platform"],
                title["duration"],title["cast"], title["country"],title["listed_in"],title["description"][0:100]+"(...)"])
    else:
        for title in lt.iterator(title):
            tabla1.add_row([title["type"],title["title"],title["release_year"],title["director"],title["streaming_platform"],
                title["duration"],title["cast"], title["country"],title["listed_in"],title["description"][0:100]+"(...)"])
    print(tabla1)
def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Lista de las películas estrenadas en un periodo de tiempo")
    print("3- Lista de programas de televisión agregados en un periodo de tiempo")
    print("4- Encontrar contenido donde participa un actor")
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
ListType = "SINGLE_LINKED"
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
    elif int(inputs) == 3:
       date1 = input("Ingrese la primera fecha: ")
       date2 = input("ingrese la segunda fecha: ")
       printReq2(control,date1,date2)
    elif int(inputs) == 4:
        actor = input("Ingrese el nombre del actor/actriz: ")
        printReq3(control,actor)
    elif int(inputs) == 10:
        control,size,algorithm,ListType = selector()
    elif int(inputs) == 11:
        sortbydate(control,algorithm,ListType)
    elif int(inputs[0]) == 0:
        sys.exit(0)

    else:
        sys.exit(0)
sys.exit(0)
