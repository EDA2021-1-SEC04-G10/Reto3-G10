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
import datetime


"""
El controlador se encarga de mediar entre la vista y el modelo
"""

# Inicialización del analizador de eventos

def initAnalyzer():
    """
    Llama la función de inicialización del analizador al modelo
    """
    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos

def loadData(analyzer):
    """
    Carga los datos de los archivos en las estructuras
    de datos
    """
    loadEvents(analyzer)

def loadEvents(analyzer):
    """
    Carga los eventos del archivo. Por cada evento se indica al
    modelo que debe adicionarlo al analizador
    """
    eventsfile = cf.data_dir + 'subsamples-small/context_content_features-small.csv'
    input_file = csv.DictReader(open(eventsfile, encoding='utf-8'))
    for event in input_file:
        model.addEvent(analyzer, event)

def loadTags(analyzer):
    """
    Carga las etiquetas del archivo. Por cada etiqueta se indica al
    modelo que debe adicionarla al analizador
    """
    tagsfile = cf.data_dir + 'subsamples-small/user_track_hashtag_timestamp-small.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for tag in input_file:
        model.addTag(analyzer, tag)

def loadSentimentValues(analyzer):
    """
    Carga los valores de sentimientos del archivo. Por cada valor se
    indica al modelo que debe adicionarlo al analizador
    """
    sentimentsfile = cf.data_dir + 'subsamples-samll/sentiment_values.csv'
    input_file = csv.DictReader(open(sentimentsfile, encoding='utf-8'))
    for sentiment in input_file:
        model.addSentimentValue(analyzer, sentiment)

# Funciones de consulta sobre el analizador

def eventsSize(analyzer):
    """
    Número de eventos cargados en el analizador
    """
    return model.eventsSize(analyzer)

def mapSize(analyzer, map):
    """
    Número de elementos del árbol
    """
    return model.mapSize(analyzer, map)

def mapHeight(analyzer, map):
    """
    Retorna la altura del árbol
    """
    return model.mapHeight(analyzer, map)

def minKey(analyzer, map):
    """
    Retorna la llave más pequeña
    """
    return model.minKey(analyzer, map)

def maxKey(analyzer, map):
    """
    Retorna la llave más grande
    """
    return model.maxKey(analyzer, map)

def getEventsByRange(analyzer, feature, initialValue, finalValue):
    """
    Retorna el número de eventos y artistas únicos por característica en un
    rango determinado de valores
    """
    return model.getEventsByRange(analyzer, feature, initialValue, finalValue)

def getEventsByTimeRange(analyzer, initialTime, finalTime):
    """
    Retorna el número de eventos en un rango determinado de tiempo en horas,
    minutos y segundos
    """
    initialTime = datetime.datetime.strptime(initialTime, '%H:%M:%S').time()
    finalTime = datetime.datetime.strptime(finalTime, '%H:%M:%S').time()
    return model.getEventsByTimeRange(analyzer, initialTime, finalTime)