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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from controller import nArtworks
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as mg
assert cf
import datetime as dt

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos..
"""
# Construccion de modelos
def newCatalog():
    catalog = {"Artist":None,
                 "Artwork":None,
                 "Medium":None }

    catalog['Artist']= lt.newList('SINGLE_LINKED', cmpfunction=compareconstituentID)

    catalog['Artwork']=lt.newList('SINGLE_LINKED', cmpfunction=compareobjectID)

#lab 5
    catalog ['Medium']=mp.newMap(21191,
                                maptype="PROBING",
                                loadfactor=0.8,
                                comparefunction=comparemedium)

#lab 6                                
    catalog ["Nationality"]=mp.newMap(119,
                                    maptype="PROBING",
                                    loadfactor=0.8,
                                    comparefunction=comparenation)
   # catalog["yearartist"]=mp.newMap(10,
   #                                maptype="PROBING",
   #                                loadfactor=0.5,
   #                                comparefunction=compareyearartist)                                
    

#Req 1
    catalog ['YearArtist']=mp.newMap(21191,
                                maptype="PROBING",
                                loadfactor=0.8,
                                comparefunction=compararAño)
    return catalog



def compareconstituentID(artist1ID, artist2ID):
 # artist1ID=int(artist1ID["ConstituentID"])
  artist2ID=int(artist2ID["ConstituentID"])
  if (artist1ID == artist2ID):
        return 0
  elif artist1ID > artist2ID:
        return 1
  else:
        return -1

def compararAño (id, tag):
  añoEntrada= me.getKey(tag)
  if (id == añoEntrada):
    return 0
  elif (id > añoEntrada):
    return 1
  else:
    return 0

def compareobjectID (artwork1ID, artwork2ID):
  artwork1ID=int(artwork1ID["ObjectID"])
  artwork1ID=int(artwork1ID["ObjectID"])
  if (artwork1ID == artwork2ID):
       return 0
  elif artwork1ID > artwork2ID:
        return 1
  else:
        return -1

def comparemedium (keymedium, medium):
  mediumentry= me.getKey(medium)
  if (keymedium == mediumentry):
    return 0
  elif (keymedium > mediumentry):
    return 1
  else:
    return -1

def comparenation (keynation, nationality):
  nationalityentry= me.getKey(nationality)
  if (keynation== nationalityentry):
    return 0
  elif (keynation>nationalityentry):
    return 1
  else:
    return -1


def addMedium(catalog, artwork):
  try:
        mediums = catalog['Medium']
        if (artwork['Medium'] != ''):
            medium = artwork['Medium']
            
        else:
            medium = "unknown"
        existmedium = mp.contains(mediums, medium)
        if existmedium:
            entry = mp.get(mediums, medium)
            listMedium = me.getValue(entry)
        else:
            listMedium = newMedium(medium)
            mp.put(mediums, medium, listMedium)
        lt.addLast(listMedium['Artworks'], artwork)
  except Exception as e:
        raise e

def newMedium(medium):
  
    entry = {'Medium': "", "Artworks": None}
    entry['Medium'] = medium
    entry['Artworks'] = lt.newList('ARRAY_LIST', comparingArtworks)
    return entry

def comparingArtworks(artwork1, artwork2):
    if (int(artwork1) == int(artwork2)):
        return 0
    elif (int(artwork1) > int(artwork2)):
        return 1
    else:
        return 0


def ancient (catalog, nartworks, medium):
  catamediums=catalog["Medium"]
  conjmediums=mp.get(catamediums,medium)
  conjmediums=me.getValue(conjmediums)["Artworks"]
  organize=sortdate(conjmediums)
  answer= lt.subList(organize,1,nartworks)
  return answer

            
def addMedium2 (tablemedium, medium,artworklist):
  try:
    #si el medio no esta en el indice
    if mp.contains (tablemedium, medium)==False and medium == artworklist["Medium"]:
      #agregar una nueva medio al indice
        mp.put(tablemedium,medium,artworklist)
    elif mp. contains(tablemedium,medium)==True and medium == artworklist["Medium"]:
      #saco los datos del medio
      temp=mp.get(tablemedium,medium)
      temp=me.getValue(temp)
      #agrego las nuevas obras a las ya existentes
      for artwork in lt.iterator(temp):
        lt.addLast(artworklist, artwork)
      #actualizar el índice de medios
      mp.put (tablemedium,medium,artworklist)
  except Exception as e:
        raise e


def addNationality (tablenationality, nationality, artworklist):
  try:
    #si la nacionalidad no esta en el indice
    #print (mp.keySet(tablenationality))
    if mp.contains(tablenationality, nationality)== False:
      #agregar una nueva nacionalidad al indice
      mp.put(tablenationality, nationality, artworklist)
      #print(lt.size(artworklist))

    #si la nacionalidad ya esta en el indice
    elif mp.contains(tablenationality, nationality)== True:
      #Saco los datos de la nacionalidad
      temp=mp.get(tablenationality, nationality)
      temp=me.getValue(temp)
      #Agrego las nuevas obras a las ya existentes
      for artwork in lt.iterator(temp):
        lt.addLast(artworklist,artwork)
        #print(artwork)
      #Actualizar indice de nacionalidades
      mp.put(tablenationality,nationality,artworklist)
      #print(lt.size(artworklist))

  except Exception as e:
        raise e

    


def artwinnation (catalog, country):
  catanation=catalog["Nationality"]
  #print(mp.size(catanation))
  conjnation=mp.get(catanation,country)
  #print(type(conjnation))
  conjnation=me.getValue(conjnation)
  #print(type(conjnation))
  return conjnation


def compareyear(date1, date2):
   if date1["BeginDate"]!= "" and date2["BeginDate"]!= "":
        year1= int((date1["BeginDate"]))
        year2= int((date2["BeginDate"]))
        return year1<year2 


# Funciones para agregar informacion al catalogo
def addartist(catalog, artists):
        artist={
             "ConstituentID": artists["ConstituentID"],
             "DisplayName": artists["DisplayName"],
             "Nationality": artists["Nationality"],
             "BeginDate":artists["BeginDate"],
             "EndDate": artists["EndDate"],
             "Gender": artists["Gender"],
             "Artworks":lt.newList("ARRAY_LIST",cmpfunction=compareobjectID)
             }
        lt.addLast(catalog["Artist"],artist)

def newYear(year):
    """
    Esta funcion crea la estructura de libros asociados
    a un año.
    """
    entry = {'YearArtist': "", 'Artworks': None}
    entry['YearArtist'] = year
    entry['Artworks'] = lt.newList('SINGLE_LINKED', compararAño)
    return entry
  

def addartwork(catalog, artworks):
        artwork={
          "ObjectID":artworks["ObjectID"],
          "Title": artworks["Title"],
          "ConstituentID": artworks["ConstituentID"],
          "Date": artworks["Date"],
          "Medium": artworks["Medium"],
          "Dimensions": artworks["Dimensions"],
          "CreditLine": artworks["CreditLine"],
          "Classification": artworks["Classification"],
          "Department": artworks["Department"],
          "DateAcquired": artworks["DateAcquired"],
          "Circumference": artworks["Circumference (cm)"],
          "Depth": artworks["Depth (cm)"],
          "Diameter": artworks["Diameter (cm)"],
          "Height": artworks["Height (cm)"],
          "Length": artworks["Length (cm)"],
          "Weight":artworks["Weight (kg)"],
          "Width": artworks["Width (cm)"],
          "Artists":lt.newList("ARRAY_LIST", cmpfunction=compareconstituentID)
          }
        lt.addLast(catalog["Artwork"],artwork)  
        IDartist= eval(artwork["ConstituentID"])
        addMedium(catalog,artwork)
        for artist in IDartist:
            addArtworkartist(catalog, artist, artwork)

      
def addArtworkartist(catalog, IDartist, artwork):
    artists=catalog["Artist"]
    position=lt.isPresent(artists, IDartist)
    if position>0:
      artist= lt.getElement(artists, position)
      lt.addLast(artist["Artworks"], artwork)
      lt.addLast(artwork["Artists"], artist)

def compareartworks(ID,artists):
    if (ID in artists["ConstituentID"]):
      return 0
    return -1


# Funciones para creacion de datos  
# REQ. 1: listar cronológicamente los artistas

def getArtistByRange(catalog, initialDate,finalDate):
    """
    Retorna artistas en un rango de años
    """
    lst = mp.values(catalog['YearArtist'], initialDate, finalDate)
    totArtist=0
    valores= {}
    for i in lt.iterator(lst):
      totArtist+= lt.size(catalog['YearArtist'])
      valores= me.getValue(lst)['years']
      return totArtist, valores


def addartistyear(catalog, year1, year2):
    artistsinrange=lt.newList("ARRAY_LIST")
    i=1
    while i<= lt.size(catalog["Artist"]):
        artist=lt.getElement(catalog["Artist"],i)
        if int(artist["BeginDate"])>= year1 and int(artist["BeginDate"])<=year2:
            lt.addLast(artistsinrange, artist)
        i+=1
    sortedlist=sortyear(artistsinrange)
    return sortedlist

  # Funciones de ordenamiento
def sortyear (artistsinrange):
        sorted_list=mg.sort(artistsinrange, cmpArtworkByBeginDate)
        return sorted_list

  # Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByBeginDate (date1, date2):
    if date1["BeginDate"]!= "" and date2["BeginDate"]!= "":
        year1= int((date1["BeginDate"]))
        year2= int((date2["BeginDate"]))
        return year1<year2 


#REQ. 2: listar cronológicamente las adquisiciones 
def addartworkyear(catalog, date1,date2):
    date1=dt.date.fromisoformat(date1)
    date2=dt.date.fromisoformat(date2)
    artworksinrange=lt.newList("ARRAY_LIST")
    i=1
    while i<= lt.size(catalog["Artwork"]):
        artwork=lt.getElement(catalog["Artwork"],i)
        if artwork["DateAcquired"]!="":
           indate=dt.date.fromisoformat(artwork["DateAcquired"])
           if indate>= date1 and indate<= date2:
               lt.addLast(artworksinrange, artwork)
        i+=1
    sortlist=sortdate(artworksinrange)
    return sortlist

  #encontrar número de obras compradas
def purchaseart (sortedlist2):
    i=1
    n=0
    while i<=lt.size(sortedlist2):
        artwork=lt.getElement(sortedlist2,i)
        if artwork["CreditLine"]=="Purchase":
            n+=1
        i+=1
    return n
    
  # Funciones de ordenamiento
def sortdate (artworksinrange):
    sorted_list=mg.sort(artworksinrange, cmpArtworkByDateAcquired)
    return sorted_list

  # Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired (artwork1, artwork2):
    if artwork1["DateAcquired"]!= "" and artwork2["DateAcquired"]!= "":
        date1= dt.date.fromisoformat(artwork1["DateAcquired"])
        date2= dt.date.fromisoformat(artwork2["DateAcquired"])
        return date1<date2


#REQ. 3: clasificar las obras de un artista por técnica (Individual)
# Total de obras
def totalartworksartist (catalog, name):
    artworks=lt.newList("ARRAY_LIST")
    for artist in lt.iterator(catalog["Artist"]):
        if artist["DisplayName"]== name:
            artworks=artist["Artworks"]
    return artworks

#Total técnicas (medios) utilizados
def totalmediums(artworks):
    techniques=lt.newList("ARRAY_LIST", cmpfunction=cmpmediums)
    j=1
    while j <=lt.size(artworks):
      artwork=lt.getElement(artworks,j)
      technique=artwork["Medium"]
      position=lt.isPresent(techniques,technique)
      if position>0:
          tec=lt.getElement(techniques, position)
          tec["value"]+=1
      else:
          tec={"Name":technique,"value":1}
          lt.addLast(techniques, tec)
      j+=1
    sortedlist=sorttecnicas(techniques)
    return sortedlist

def sorttecnicas(techniques):
   sortedlist=mg.sort(techniques, cmptechniques)
   return sortedlist

def cmptechniques( technique1, technique2):
    if technique1["value"]>=technique2["value"]:
       return True
    else:
       return False
  
def cmpmediums (technique1,technique2):
  if technique1== technique2["Name"]:
    return 0
  else:
    return 1

#La técnica mas utilizada  
def firsttechnique (sortedlist):
   name=lt.firstElement(sortedlist)
   name=name["Name"]
   return name

#El listado de las obras de dicha técnica
def artworkstechnique1(name,artworks):
  listartworks=lt.newList("ARRAY_LIST")
  for artwork in lt.iterator(artworks):
    if artwork["Medium"]==name:
      lt.addLast(listartworks,artwork)
  return listartworks

#REQ. 4:clasificar las obras por la nacionalidad de sus creadores

def take (n, iterable):
  return list(islice(iterable,n))

def recurrentartworks (catalog , top):
  id = catalog["Artist"]
  list= lt.newList(datastructure= "ARRAY_LIST")

  for artist in id.values():
    nationality = artist["Nationality"]
    if nationality == top:
      for artwork in lt.iterator(artist["Artworks"]):
        lt.addLast(list, artwork)
  return list

def tenNationalities (catalog):
  dictionary = {}
  identification = catalog["Artist"]

  for artist in identification.values():
    size= lt.size(artist["Artworks"])
    nationality= artist["Nationality"]

    if nationality != "" or nationality != "Nationality unknown":
      if nationality not in dictionary.keys():
        dictionary["Nationality"]= size
      else:
        dictionary["Nationality"]+= size

  organized= dict(sorted(dictionary.items(),key=lambda item:item[1], reverse= True))

  nationalities= take(100, organized.items())
  first= nationalities[0][0]
  list= recurrentartworks(catalog, first)
    
  return nationalities, list

def artworkstechnique (name,artworks):
  listartworks=lt.newList("ARRAY_LIST")
  for artwork in lt.iterator(artworks):
    if artwork["Medium"]==name:
      lt.addLast(listartworks,artwork)
  return listartworks
  


#REQ. 5: transportar obras de un departamento
#Total de obras para transportar (size de esto)
def totalartworks(catalog, depto):
   listartworks= lt.newList("ARRAY_LIST")
   artworks=catalog["Artwork"]
   for artwork in lt.iterator(artworks):
     if artwork["Department"]==depto:
       lt.addLast(listartworks,artwork)
   return listartworks

#Estimado en USD del precio del servicio
def price (listartworks):
    totalprice=0
    cost=72
    for artwork in lt.iterator(listartworks):
       kgprice=0
       m2price1=0
       m2price2=0
       m2price3=0
       m2price4=0
       m2price5=0
       m2price6=0
       m2price7=0
       m2price8=0
       m2price9=0
       m3price1=0
       m3price2=0
       m3price3=0
       m3price4=0
       m3price5=0
       m3price6=0
       m3price7=0
       m3price8=0
       weight=artwork["Weight"]
       diameter=artwork["Diameter"]
       circumference=artwork["Circumference"]
       length=artwork["Length"]
       height=artwork["Height"]
       width=artwork["Width"]
       depth=artwork["Depth"]
       if weight !="" :
         kgprice=float(weight)*cost
       if height!= "" and width!= "":
         m2price1=(float(height)/100)*(float(width)/100)*cost
       if height!= "" and length!= "":
         m2price2=(float(height)/100)*(float(length)/100)*cost
       if height!= "" and depth!= "":
         m2price3=(float(height)/100)*(float(depth)/100)*cost
       if length!= "" and width != "":
         m2price4= (float(length)/100)*(float(width)/100)*cost
       if depth!="" and width!="":
         m2price5= (float(depth)/100)*(float(width)/100)*cost
       if length!="" and depth!="":
         m2price6= (float(length)/100)*(float(depth)/100)*cost
       if diameter !="":
         m2price8=3.1416*(((float(diameter)/2)/100)**2)*cost
       if circumference!="":
         m2price9= 3.1416*(((float(circumference)/100)/(2*3.1416))**2)*cost

       if length!="" and width != "" and depth != "":
         m3price1=(float(length)/100)*(float(width)/100)*(float(depth)/100)*cost
       if height!="" and width!= "" and depth!= "":
         m3price2=(float(height)/100)*(float(width)/100)*(float(depth)/100)*cost
       if height!="" and width!= "" and length!= "":
         m3price3=(float(height)/100)*(float(width)/100)*(float(length)/100)*cost
       if length!="" and depth!= "" and height!= "":
         m3price4=(float(length)/100)*(float(depth)/100)*(float(height)/100)*cost
       if height!="" and diameter!= "":
         m3price5=3.1416*((((float(diameter))/2)/100)**2)*(float(height)/100)*cost
       if width!="" and diameter!="":
         m3price6=3.1416*((((float(diameter))/2)/100)**2)*(float(width)/100)*cost
       if depth!="" and diameter!="":
         m3price7=3.1416*((((float(diameter))/2)/100)**2)*(float(depth)/100)*cost
       if length!="" and diameter!="":
         m3price8=3.1416*((((float(diameter))/2)/100)**2)*(float(length)/100)*cost
       lastprice= max(kgprice,m2price1,m2price2,m2price3,m2price4,m2price5,m2price6,m2price7,m2price8,m2price9,m3price1,m3price2,m3price3,m3price4,m3price5,m3price6,m3price7,m3price8)
       if lastprice==0:
         lastprice=48
       artwork["Price"]=lastprice
       totalprice+=lastprice
    return (totalprice, listartworks)

#Peso estimado de las obras
def weight (listartworks):
  weight=0
  for artwork in lt.iterator(listartworks):
    artweight=artwork["Weight"]
    if artweight== "":
      weight+=0
    else:
      artweightinfloat=float(artweight)
      weight+=artweightinfloat
  return weight

#Obras viejas
def oldest (listartworks):
  sortedlist=sortoldest(listartworks)
  return sortedlist

def sortoldest (listartworks):
  sorted_list=mg.sort(listartworks, cmpoldest)
  return sorted_list

def cmpoldest(date1, date2):
  if date1["Date"]!="" and date2["Date"]!="":
    date1=int(date1["Date"])
    date2=int(date2["Date"])
    return date1>date2

#mas costosas
def expensive(listartworks):
  sortlist=sortexpensive(listartworks)
  return sortlist

def sortexpensive(listartworks):
  sort_list=mg.sort(listartworks, cmpexpensive)
  return sort_list

def cmpexpensive(price1,price2):
  pricevalue1=price1["Price"]
  pricevalue2=price2["Price"]
  return pricevalue1>pricevalue2

