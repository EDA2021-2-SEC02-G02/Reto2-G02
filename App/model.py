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
                                 
#Req 1
    catalog ['YearArtist']=mp.newMap(2000,
                                maptype="PROBING",
                                loadfactor=0.5,
                                comparefunction=compareMapYear)


#Req 2
    catalog ['yearartworks']=mp.newMap(67760,
                                maptype="PROBING",
                                loadfactor=0.98,
                                comparefunction=compareyearreq2)
                      
#Req 3
    catalog["Nameartist"]=mp.newMap(15166,
                                    maptype="CHAINING",
                                    loadfactor=1,
                                    comparefunction=comparename)
                            
#Req 5
    catalog["Departmentart"]=mp.newMap(15166,
                                    maptype="CHAINING",
                                    loadfactor=0.75,
                                    comparefunction=comparedepartment)
    return catalog



def compareconstituentID(artist1ID, artist2ID):
  artist2ID=int(artist2ID["ConstituentID"])
  if (artist1ID == artist2ID):
        return 0
  elif artist1ID > artist2ID:
        return 1
  else:
        return -1

def compareobjectID (artwork1ID, artwork2ID):
  artwork1ID=int(artwork1ID["ObjectID"])
  artwork1ID=int(artwork1ID["ObjectID"])
  if (artwork1ID == artwork2ID):
       return 0
  elif artwork1ID > artwork2ID:
        return 1
  else:
        return -1

#req1 -------------------------------------------------------------------
def compareMapYear(id, year):
    yearentry = me.getKey(year)
    if (id == yearentry):
        return 0
    elif (id > yearentry):
        return 1
    else:
        return 0

def compararAño (year1, year2):

  if (int(year1) == int(year2)):
    return 0
  elif (int(year1) > int(year2)):
    return 1
  else:
    return 0

#Req 2
def compareyearreq2 (keyyear, year):
  yearentry=me.getKey(year)
  if (keyyear==yearentry):
    return 0
  elif (keyyear>yearentry):
    return 1
  else:
    return -1 

#Req 3
def comparename (keyname, name):
  nameentry=me.getKey(name)
  if (keyname==nameentry):
    return 0
  elif (keyname>nameentry):
    return 1
  else:
    return -1

#Req 5
def comparedepartment (keydepto, depto):
  deptoentry=me.getKey(depto)
  if(keydepto==deptoentry):
    return 0
  elif (keydepto>deptoentry):
    return 1
  else:
    return -1



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

#Carga de indices
#req1-----------------------------------------------------------------------
def newYear(year):
   
    entry = {'YearArtist': "","Artist": None}
    entry['YearArtist'] = year
    entry["Artist"] = lt.newList('SINGLE_LINKED', compararAño)
    return entry


#req 2
def adddatereq2 (tabledate, dateacquired, artwork):
  try:
    #si le fecha no esta en el indice
    if dateacquired != "" and mp.contains(tabledate, dateacquired)==False:
      #agregar nueva fecha al indice
      artworklist=lt.newList("ARRAY_LIST")
      lt.addLast(artworklist,artwork)
      mp.put (tabledate, dateacquired, artworklist)
    #si la nacionalidad ya esta en el índice
    elif  mp.contains(tabledate, dateacquired)==True:
      #saco los datos de la fecha
      temp=mp.get(tabledate, dateacquired)
      tempo=me.getValue(temp)
      #Agrego la nueva obra a las ya existentes
      lt.addLast (tempo, artwork)
  except Exception as e:
        raise e

def comparedate(date1, date2):
  date1=dt.date.fromisoformat(date1)
  date2=dt.date.fromisoformat(date2)
  if date1["BeginDate"]!= "" and date2["BeginDate"]!= "":
        year1= int((date1["BeginDate"]))
        year2= int((date2["BeginDate"]))
        return year1<year2 

#req3
def addnames(tablename, name, artworklist):
  try:
    #si el nombre no esta en el indice
    if name != "" and mp.contains(tablename, name)==False: 
      #agregar nuevo nombre al indice
      mp.put(tablename, name, artworklist)
  except Exception as e:
        raise e

#req5
def adddepto (tabledepto, depto, artwork):
  try:
    #si el depto no esta en el indice
    if depto!= "" and mp.contains(tabledepto, depto)==False:
      #agregar nuevo departamento al indice
      artworklist=lt.newList("ARRAY LIST", compareconstituentID)
      lt.addLast(artworklist,artwork)
      mp.put(tabledepto, depto, artworklist)
    #si el departamento ya esta en el indice
    elif mp.contains (tabledepto,depto)==True:
      temp=mp.get (tabledepto,depto)
      temp=me.getValue(temp)
      lt.addLast(temp, artwork)
  except Exception as e:
        raise e


# Funciones para creacion de datos  
# REQ. 1: listar cronológicamente los artistas

def getArtistByRange(catalog, initialDate,finalDate):
    """
    Retorna artistas en un rango de años
    """
    artistInRange =lt.newList("ARRAY_LIST")

    keys= mp.keySet(catalog["YearArtist"])

    for año in lt.iterator(keys):
      if int(año) >= int(initialDate) and int(año) <= int(finalDate):
        entry= mp.get (catalog["YearArtist"],año)
        valor= me.getValue(entry)
        artist= valor["Artist"]
        for artista in lt.iterator(artist):
          lt.addLast(artistInRange, artista)  
    sortedlist=sortyear(artistInRange)

    return sortedlist

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
  yearcatalog=catalog["yearartworks"]
  listtemp=mp.keySet(yearcatalog)
  sortlist=mg.sort(listtemp, compareadcquireddate)
  for date in lt.iterator(sortlist):
    datestr=date
    date=dt.date.fromisoformat(date)
    if date >= date1 and date <= date2:
      temp=mp.get(yearcatalog,datestr)
      temp=me.getValue(temp)
      for artwork in lt.iterator(temp):
        lt.addLast(artworksinrange,artwork)
  return artworksinrange

def compareadcquireddate(date1, date2):
  if date1!= "" and date2!= "":
    date1=dt.date.fromisoformat(date1)
    date2=dt.date.fromisoformat(date2)
    return date1<date2
  
  

#encontrar número de obras compradas
def purchaseart (sortedlist2):
  n=0
  for artwork in lt.iterator(sortedlist2):
    if "Purchase" in  artwork["CreditLine"] :
      n+=1
  return n
    



#REQ. 3: clasificar las obras de un artista por técnica (Individual)
# Total de obras
def totalartworksartist (catalog, name):
    catalogname= catalog["Nameartist"]
    artistindex= mp.get(catalogname,name)
    artworksartist= me.getValue (artistindex)
    return artworksartist

#Total técnicas (medios) utilizados
def totalmediums(artworksartist):
    techniques=lt.newList("ARRAY_LIST", cmpfunction=cmpmediums)
    for artwork in lt.iterator(artworksartist):
      technique=artwork["Medium"]
      position=lt.isPresent(techniques,technique)
      if position>0:
          tec=lt.getElement(techniques, position)
          tec["value"]+=1
      else:
          tec={"Name":technique,"value":1}
          lt.addLast(techniques, tec)
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
   deptomap=catalog["Departmentart"]
   indexdepto=mp.get(deptomap, depto)
   artworksdepto=me.getValue(indexdepto)
   return artworksdepto

#Estimado en USD del precio del servicio
def price (artworksdepto):
    totalprice=0
    cost=72
    for artwork in lt.iterator(artworksdepto):
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
    return (totalprice, artworksdepto)

#Peso estimado de las obras
def weight (artworksdepto):
  weight=0
  for artwork in lt.iterator(artworksdepto):
    artweight=artwork["Weight"]
    if artweight== "":
      weight+=0
    else:
      artweightinfloat=float(artweight)
      weight+=artweightinfloat
  return weight

#Obras viejas
def oldest (artworksdepto):
  sortedlist=sortoldest(artworksdepto)
  return sortedlist

def sortoldest (artworksdepto):
  sorted_list=mg.sort(artworksdepto, cmpoldest)
  return sorted_list

def cmpoldest(date1, date2):
  if date1["Date"]!="" and date2["Date"]!="":
    date1=int(date1["Date"])
    date2=int(date2["Date"])
    return date1>date2

#mas costosas
def expensive(artworksdepto):
  sortlist=sortexpensive(artworksdepto)
  return sortlist

def sortexpensive(artworksdepto):
  sort_list=mg.sort(artworksdepto, cmpexpensive)
  return sort_list

def cmpexpensive(price1,price2):
  pricevalue1=price1["Price"]
  pricevalue2=price2["Price"]
  return pricevalue1>pricevalue2

