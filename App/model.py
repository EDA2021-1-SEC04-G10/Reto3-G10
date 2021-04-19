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
    tracks
    artists
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
                'tracks': None,
                'artists': None,
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
    Este índice crea un map cuya llave es el identificador del track
    """
    analyzer['tracks'] = om.newMap('RBT')

    """
    Este índice crea un map cuya llave es el identificador del artist
    """
    analyzer['artists'] = om.newMap('RBT')

    """
    Este índice crea un map cuya llave es el valor de instrumentalness
    """
    analyzer['instrumentalness'] = om.newMap('RBT', compareValues)

    """
    Este índice crea un map cuya llave es el valor de liveness
    """
    analyzer['liveness'] = om.newMap('RBT', compareValues)

    """
    Este índice crea un map cuya llave es el valor de speechiness
    """
    analyzer['speechiness'] = om.newMap('RBT', compareValues)

    """
    Este índice crea un map cuya llave es el valor de danceability
    """
    analyzer['danceability'] = om.newMap('RBT', compareValues)

    """
    Este índice crea un map cuya llave es el valor de valence
    """
    analyzer['valence'] = om.newMap('RBT', compareValues)

    """
    Este índice crea un map cuya llave es el valor de loudness
    """
    analyzer['loudness'] = om.newMap('RBT', compareValues)

    """
    Este índice crea un map cuya llave es el valor de tempo
    """
    analyzer['tempo'] = om.newMap('RBT', compareValues)

    """
    Este índice crea un map cuya llave es el valor de acousticness
    """
    analyzer['acousticness'] = om.newMap('RBT', compareValues)

    """
    Este índice crea un map cuya llave es el valor de energy
    """
    analyzer['energy'] = om.newMap('RBT', compareValues)

    return analyzer

# Funciones para agregar información al analizador

def addEvent(analyzer, event):
    """
    Adiciona un evento a la lista de eventos
    """
    lt.addLast(analyzer['events'], event)
    addTracks(analyzer, event)
    addArtists(analyzer, event)
    updateInstrumentalness(analyzer, event)
    updateLiveness(analyzer, event)
    updateSpeechiness(analyzer, event)
    updateDanceability(analyzer, event)
    updateValence(analyzer, event)
    updateLoudness(analyzer, event)
    updateTempo(analyzer, event)
    updateAcousticness(analyzer, event)
    updateEnergy(analyzer, event)

def addTracks(analyzer, event):
    """
    """
    tracks = analyzer['tracks']
    track = event['track_id']
    existtrack = om.contains(tracks, track)
    if existtrack:
        entry = om.get(tracks, track)
        value = me.getValue(entry)
    else:
        value = newValue(track, 'track')
        om.put(tracks, track, value)
    lt.addLast(value['events'], event)

def addArtists(analyzer, event):
    """
    """
    artists = analyzer['artists']
    artist = event['artist_id']
    existartist = om.contains(artists, artist)
    if existartist:
        entry = om.get(artists, artist)
        value = me.getValue(entry)
    else:
        value = newValue(artist, 'artist')
        om.put(artists, artist, value)
    lt.addLast(value['events'], event)

def updateInstrumentalness(analyzer, event):
    """
    """
    values = analyzer['instrumentalness']
    instrumentalness = float(event['instrumentalness'])
    existvalue = om.contains(values, instrumentalness)
    if existvalue:
        entry = om.get(values, instrumentalness)
        value = me.getValue(entry)
    else:
        value = newValue(instrumentalness, 'instrumentalness')
        om.put(values, instrumentalness, value)
    lt.addLast(value['events'], event)

def updateLiveness(analyzer, event):
    """
    """
    values = analyzer['liveness']
    liveness = float(event['liveness'])
    existvalue = om.contains(values, liveness)
    if existvalue:
        entry = om.get(values, liveness)
        value = me.getValue(entry)
    else:
        value = newValue(liveness, 'liveness')
        om.put(values, liveness, value)
    lt.addLast(value['events'], event)

def updateSpeechiness(analyzer, event):
    """
    """
    values = analyzer['speechiness']
    speechiness = float(event['speechiness'])
    existvalue = om.contains(values, speechiness)
    if existvalue:
        entry = om.get(values, speechiness)
        value = me.getValue(entry)
    else:
        value = newValue(speechiness, 'speechiness')
        om.put(values, speechiness, value)
    lt.addLast(value['events'], event)

def updateDanceability(analyzer, event):
    """
    """
    values = analyzer['danceability']
    danceability = float(event['danceability'])
    existvalue = om.contains(values, danceability)
    if existvalue:
        entry = om.get(values, danceability)
        value = me.getValue(entry)
    else:
        value = newValue(danceability, 'danceability')
        om.put(values, danceability, value)
    lt.addLast(value['events'], event)

def updateValence(analyzer, event):
    """
    """
    values = analyzer['valence']
    valence = float(event['valence'])
    existvalue = om.contains(values, valence)
    if existvalue:
        entry = om.get(values, valence)
        value = me.getValue(entry)
    else:
        value = newValue(valence, 'valence')
        om.put(values, valence, value)
    lt.addLast(value['events'], event)

def updateLoudness(analyzer, event):
    """
    """
    values = analyzer['loudness']
    loudness = float(event['loudness'])
    existvalue = om.contains(values, loudness)
    if existvalue:
        entry = om.get(values, loudness)
        value = me.getValue(entry)
    else:
        value = newValue(loudness, 'loudness')
        om.put(values, loudness, value)
    lt.addLast(value['events'], event)

def updateTempo(analyzer, event):
    """
    """
    values = analyzer['tempo']
    tempo = float(event['tempo'])
    existvalue = om.contains(values, tempo)
    if existvalue:
        entry = om.get(values, tempo)
        value = me.getValue(entry)
    else:
        value = newValue(tempo, 'tempo')
        om.put(values, tempo, value)
    lt.addLast(value['events'], event)

def updateAcousticness(analyzer, event):
    """
    """
    values = analyzer['acousticness']
    acousticness = float(event['acousticness'])
    existvalue = om.contains(values, acousticness)
    if existvalue:
        entry = om.get(values, acousticness)
        value = me.getValue(entry)
    else:
        value = newValue(acousticness, 'acousticness')
        om.put(values, acousticness, value)
    lt.addLast(value['events'], event)

def updateEnergy(analyzer, event):
    """
    """
    values = analyzer['energy']
    energy = float(event['energy'])
    existvalue = om.contains(values, energy)
    if existvalue:
        entry = om.get(values, energy)
        value = me.getValue(entry)
    else:
        value = newValue(energy, 'energy')
        om.put(values, energy, value)
    lt.addLast(value['events'], event)

# Funciones para creación de datos

def newValue(value, feature):
    """
    Crea un nodo en el árbol por característica de contenido
    """
    value = {'feature': '',
             'events': None}
    
    value['feature'] = feature
    value['events'] = lt.newList('ARRAY_LIST')
    return value

# Funciones de consulta

def eventsSize(analyzer):
    """
    Número de videos cargados en el analizador
    """
    return lt.size(analyzer['events'])

def mapSize(analyzer, map):
    """
    Número de elementos en el árbol
    """
    return om.size(analyzer[map])

def mapHeight(analyzer, map):
    """
    Retorna la altura del árbol
    """
    return om.height(analyzer[map])

def minKey(analyzer, map):
    """
    Retorna la llave más pequeña
    """
    return om.minKey(analyzer[map])

def maxKey(analyzer, map):
    """
    Retorna la llave más grande
    """
    return om.maxKey(analyzer[map])

def getEventsByRange(analyzer, feature, initialValue, finalValue):
    """
    Retorna el número de eventos por característica en un rango determinado
    de valores
    """
    lst = om.values(analyzer[feature], initialValue, finalValue)
    totalevents = 0
    for event in lt.iterator(lst):
        totalevents += lt.size(event['events'])
    return totalevents

# Funciones utilizadas para comparar elementos

def compareValues(value1, value2):
    """
    Compara los valores de dos eventos
    """
    if (value1 == value2):
        return 0
    elif (value1 > value2):
        return 1
    else:
        return -1

# Funciones de ordenamiento