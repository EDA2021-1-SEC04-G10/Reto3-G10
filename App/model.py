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
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf


"""
Se define la estructura de un analizador de eventos. El analizador tendrá una lista para los eventos
de escucha
"""

# Construcción de modelos

def newAnalyzer():
    """
    Inicializa el analizador de eventos. Crea una lista para guardar
    los eventos. Se crean índices (maps) por los siguientes
    criterios:
    instrumentalness
    liveness
    speechiness
    danceacibility
    valence
    loudness
    tempo
    acousticness
    energy
    """
    analyzer = {'events': None,
                'instrumentalness': None,
                'liveness': None,
                'speechiness': None,
                'danceability': None,
                'valence': None,
                'loudness': None,
                'tempo': None,
                'acousticness': None,
                'energy': None}

    """
    Esta lista contiene los eventos del archivo. Los eventos son
    referenciados por los índices creados a continuación
    """
    analyzer['events'] = lt.newList('ARRAY_LIST')

    """
    Se crean índices (maps) por diferentes criterios para llegar
    a la información consultada
    """

    """
    Este índice crea un map cuya llave es el valor de instrumentalness
    """
    analyzer['instrumentalness'] = om.newMap('RBT')

    """
    Este índice crea un map cuya llave es el valor de liveness
    """
    analyzer['liveness'] = om.newMap('RBT')

    """
    Este índice crea un map cuya llave es el valor de speechiness
    """
    analyzer['speechiness'] = om.newMap('RBT')

    """
    Este índice crea un map cuya llave es el valor de danceability
    """
    analyzer['danceability'] = om.newMap('RBT')

    """
    Este índice crea un map cuya llave es el valor de valence
    """
    analyzer['valence'] = om.newMap('RBT')

    """
    Este índice crea un map cuya llave es el valor de loudness
    """
    analyzer['loudness'] = om.newMap('RBT')

    """
    Este índice crea un map cuya llave es el valor de tempo
    """
    analyzer['tempo'] = om.newMap('RBT')

    """
    Este índice crea un map cuya llave es el valor de acousticness
    """
    analyzer['acousticness'] = om.newMap('RBT')

    """
    Este índice crea un map cuya llave es el valor de energy
    """
    analyzer['energy'] = om.newMap('RBT')

    return analyzer

# Funciones para agregar información al analizador

def addEvent(analyzer, event):
    """
    Adiciona un evento a la lista de eventos
    """
    lt.addLast(analyzer['events'], event)

# Funciones para creación de datos

# Funciones de consulta

def eventsSize(analyzer):
    """
    Número de videos cargados en el analizador
    """
    return lt.size(analyzer['events'])

# Funciones utilizadas para comparar elementos

# Funciones de ordenamiento
