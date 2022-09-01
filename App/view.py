﻿"""
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
def newController():
    """
        Se crea una instancia del controlador
    """
    control = controller.newController()
    return control

def loadData(control):
    Amazon,Disney,Hulu,Netflix = controller.loadData(control)

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
    size,first_three,last_three = controller.TitleByTime(control,date1,date2)
    print("Hay "+str(size),"'TV SHOW' entre "+date1,"y " + date2+".")
    print("Los Primeros y ultimos 3 programas son:\n" + str(first_three),str(last_three))
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
    print("0- Salir")

control = newController()

"""
Menu principal
"""





while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        Data = loadData(control)
        PrintStreamingData(Data)
    if int(inputs[0]) == 2:
       date1 = input("Ingrese la primera fecha: ")
       date2 = input("ingrese la segunda fecha: ")
       printReq2(control,date1,date2)
    elif int(inputs[0]) == 0:
        sys.exit(0)
    else:
        continue
sys.exit(0)
