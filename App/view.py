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
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada selección
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

# Funciones para la impresión de resultados

def printFirstEvents(analyzer, sample):
    """
    Imprime la información de los primeros eventos de escucha
    cargados en el analizador
    """
    size = lt.size(analyzer['events'])
    if size > sample:
        index = 1
        print("Los primeros " + str(sample) + " eventos de escucha cargados son: ")
        while index <= sample:
            event = lt.getElement(analyzer['events'], index)
            print("Track " + str(index) + ": " + str(event['track_id']))
            index += 1
        print()

def printLastEvents(analyzer, sample):
    """
    Imprime la información de los últimos eventos de escucha
    cargados en el analizador
    """
    size = lt.size(analyzer['events'])
    if size > sample:
        index = size - (sample - 1)
        print("Los últimos " + str(sample) + " eventos de escucha cargados son: ")
        while index <= size:
            event = lt.getElement(analyzer['events'], index)
            print("Track " + str(index) + ": " + str(event['track_id']))
            index += 1
        print()

# Menu de opciones

def printMenu():
    print("Bienvenido")
    print("1- Inicializar analizador")
    print("2- Cargar información de los eventos")
    print("3- Consultar eventos por característica en un rango")
    print("4- Consultar pistas por energy y danceability")
    print("5- Consultar pistas por instrumentalness y tempo")
    print("6- Consultar pistas y artistas por género")
    print("7- Consultar género más escuchado en un rango de horas")
    print("0- Salir")

# Funciones de inicialización

def initAnalyzer():
    """
    Inicializa el analizador de eventos
    """
    return controller.initAnalyzer()

def loadData(analyzer):
    """
    Carga la información de los eventos al analizador
    """
    return controller.loadData(analyzer)

analyzer = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print()
        print("Inicializando....\n")
        analyzer = initAnalyzer()

    elif int(inputs[0]) == 2:
        print()
        print("Cargando información de los eventos....")
        data = loadData(analyzer)
        print("Total de eventos de escucha cargados: " + str(controller.eventsSize(analyzer)))
        print("Total de artistas cargados: " + str(controller.mapSize(analyzer, 'artists')))
        print("Total de pistas de audio cargadas: " + str(controller.mapSize(analyzer, 'tracks')) + "\n")
        printFirstEvents(analyzer, 5)
        printLastEvents(analyzer, 5)

    elif int(inputs[0]) == 3:
        print()
        feature = str(input("Ingrese característica de contenido: "))
        initialValue = float(input("Valor inicial: "))
        finalValue = float(input("Valor final: "))
        print("\nBuscando eventos de escucha entre " + str(initialValue) + " y " + str(finalValue) + "....")
        events = controller.getEventsByRange(analyzer, feature, initialValue, finalValue)
        print("\nTotal de eventos para " + str(feature) + " en el rango de valores: " + str(events[0]))
        print("Total de artistas únicos en el rango de valores: " + str(events[1]))
        print("\nAltura del árbol: " + str(controller.mapHeight(analyzer, feature)))
        print("Elementos del árbol: " + str(controller.mapSize(analyzer, feature)))
        print("Menor llave: " + str(controller.minKey(analyzer, feature)))
        print("Mayor llave: " + str(controller.maxKey(analyzer, feature)) + "\n")

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        pass

    elif int(inputs[0]) == 7:
        pass

    else:
        sys.exit(0)
sys.exit(0)