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
from DISClib.ADT import list as lt


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initcatalog():
    catalog=model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loaddata(catalog):
    try:
        loadartists(catalog)
        loadartworks(catalog)
        load_tables(catalog)
    except Exception as e:
        raise e

def loadartists(catalog):
    artistfile=cf.data_dir+"Artists-utf8-small.csv"
    input_file=csv.DictReader(open(artistfile,encoding="utf-8"))
    for artist in input_file:
        model.addartist(catalog,artist)

def loadartworks(catalog):
    artworksfile=cf.data_dir+"Artworks-utf8-small.csv"
    input_file=csv.DictReader(open(artworksfile,encoding="utf-8"))
    for artwork in input_file:
        model.addartwork(catalog,artwork)

def load_tables(catalog):
    #Cargando lista de artistas e indice de nacionalidades de obras
    for artist in lt.iterator(catalog["Artist"]):
        nationality=artist["Nationality"]
        tablenationality=catalog["Nationality"]
        artworklist=artist["Artworks"]
        model.addNationality(tablenationality, nationality, artworklist)

    #Cargando lista de obras req2  
    for artwork in lt.iterator (catalog["Artwork"]):
        dateacquired=artwork["DateAcquired"]
        tabledate= catalog["yearartworks"]
        model.adddatereq2(tabledate, dateacquired, artwork)
    
    #cargando lista de obras req3
    for artist in lt.iterator(catalog["Artist"]):
        name=artist["DisplayName"]
        tablename=catalog["Nameartist"]
        artworklist=artist["Artworks"]
        model.addnames(tablename, name, artworklist)

    #cargando lista de obras req5
    for artwork in lt.iterator(catalog["Artwork"]):
        depto=artwork["Department"]
        tabledepto=catalog["Departmentart"]
        model.adddepto(tabledepto, depto, artwork)

# Funciones de ordenamiento
# REQ. 1: listar cronológicamente los artistas 
def addartistyear(catalog, year1, year2):
    return model.addartistyear(catalog, year1, year2)




#REQ. 2: listar cronológicamente las adquisiciones 
def addartworkyear(catalog, date1, date2):
    return model.addartworkyear(catalog, date1, date2)

def purchaseart(list2):
    return model.purchaseart(list2)


#REQ. 3: clasificar las obras de un artista por técnica (Individual)
def totalartworksartist(catalog, name):
    return model.totalartworksartist(catalog, name)

def totalmediums(artworks):
    return model.totalmediums(artworks)

def firsttechnique(sortedlist):
    return model.firsttechnique(sortedlist)

def artworkstechnique1(name, artworks):
    return model.artworkstechnique1(name, artworks)


# REQ. 4: clasificar las obras por la nacionalidad de sus creadores
def artworksNationality(catalog):
    return model.tenNationalities(catalog)


#REQ. 5: transportar obras de un departamento
def totalartworks(catalog, depto):
    return model.totalartworks(catalog, depto)

def price(listartworks):
    return model.price(listartworks)

def weight(listartworks):
    return model.weight(listartworks)

def oldest(listartworks):
    return model.oldest(listartworks)

def expensive(listartworks):
    return model.expensive(listartworks)

