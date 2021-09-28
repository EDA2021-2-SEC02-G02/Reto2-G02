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

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
# Construccion de modelos
def newCatalog():
    catalog = {"Artista":None,
                 "Obra":None,
                 "Medio":None }

    catalog['Artista']= lt.newList('SINGLE_LINKED', compareconstituentID)

    catalog['Obra']=lt.newList('SINGLE_LINKED', compareobjectID)

    catalog ['Medio']=mp.newMap(20,
                                maptype="CHAINING",
                                loadfactor=0.75,
                                comparefunction=comparemedium)

    return catalog


def compareconstituentID(artist1ID, artist2ID):
  if (artist1ID == artist2ID):
        return 0
  elif len(artist1ID) > len(artist2ID):
        return 1
  else:
        return -1

def compareobjectID (artwork1ID, artwork2ID):
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



def addMedio(catalog, obra):
  try:
        medios = catalog['Medio']
        if (obra['Medium'] != ''):
            medio = obra['Medium']
            
        else:
            medio = "desconocido"
        existmedio = mp.contains(medios, medio)
        if existmedio:
            entry = mp.get(medios, medio)
            listaMedio = me.getValue(entry)
        else:
            listaMedio = newMedio(medio)
            mp.put(medios, medio, listaMedio)
        lt.addLast(listaMedio['Obras'], obra)
  except Exception:
        return None

def newMedio(medio):
    """
    Esta funcion crea la estructura de libros asociados
    a un año.
    """
    entry = {'Medio': "", "Obras": None}
    entry['Medio'] = medio
    entry['Obras'] = lt.newList('ARRAY_LIST', compararObras)
    return entry

def compararObras(obra1, obra2):
    if (int(obra1) == int(obra2)):
        return 0
    elif (int(obra1) > int(obra2)):
        return 1
    else:
        return 0


def antiguas (catalog, nobras, medio):
  catamedios=catalog["Medio"]
  print(catamedios)
  conjmedios=mp.get(catamedios,medio)
  conjmedios=me.getValue(conjmedios)["Obras"]
  organizar=sortyear(conjmedios)
  return organizar

def compareyear(date1, date2):
   if date1["BeginDate"]!= "" and date2["BeginDate"]!= "":
        year1= int((date1["BeginDate"]))
        year2= int((date2["BeginDate"]))
        return year1<year2 


# Funciones para agregar informacion al catalogo
def addartista(catalog, artistas):
        artista={"ConstituentID": artistas["ConstituentID"],
             "DisplayName": artistas["DisplayName"],
             "Nationality": artistas["Nationality"],
             "BeginDate":artistas["BeginDate"],
             "EndDate": artistas["EndDate"],
             "Gender": artistas["Gender"],
             "Artworks":lt.newList("ARRAY_LIST")}
        lt.addLast(catalog["Artista"],artista)
  

def addobra(catalog, obras):
        obra={"ObjectID":obras["ObjectID"],
          "Title": obras ["Title"],
          "ConstituentID": obras ["ConstituentID"][1:-1],
          "Date": obras["Date"],
          "Medium": obras["Medium"],
          "Dimensions": obras["Dimensions"],
          "CreditLine": obras["CreditLine"],
          "Classification": obras["Classification"],
          "Department": obras["Department"],
          "DateAcquired": obras["DateAcquired"],
          "Circumference": obras["Circumference (cm)"],
          "Depth": obras["Depth (cm)"],
          "Diameter": obras["Diameter (cm)"],
          "Height": obras["Height (cm)"],
          "Length": obras["Length (cm)"],
          "Weight":obras["Weight (kg)"],
          "Width": obras["Width (cm)"],
          "Artists":lt.newList("ARRAY_LIST")}
        lt.addLast(catalog["Obra"],obra)  
        IDartista= obra["ConstituentID"].split(",")
        addMedio(catalog,obra)
        for artista in IDartista:
            addArtworkartist(catalog, artista, obra)

      
def addArtworkartist(catalog, IDartista, obra):
    artistas=catalog["Artista"]
    posicion=lt.isPresent(artistas, IDartista)
    if posicion>0:
      artista= lt.getElement(artistas, posicion)
      lt.addLast(artista["Artworks"], obra)
      lt.addLast(obra["Artists"], artista)

def compareartworks(ID,artistas):
    if (ID in artistas["ConstituentID"]):
      return 0
    return -1


# Funciones para creacion de datos  
# REQ. 1: listar cronológicamente los artistas  
 
def addartistyear(catalog, año1, año2):
    artistsinrange=lt.newList("ARRAY_LIST")
    i=1
    while i<= lt.size(catalog["Artista"]):
        artista=lt.getElement(catalog["Artista"],i)
        if int(artista["BeginDate"])>= año1 and int(artista["BeginDate"])<=año2:
            lt.addLast(artistsinrange, artista)
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
def addartworkyear(catalog, fecha1,fecha2):
    fecha1=dt.date.fromisoformat(fecha1)
    fecha2=dt.date.fromisoformat(fecha2)
    artworksinrange=lt.newList("ARRAY_LIST")
    i=1
    while i<= lt.size(catalog["Obra"]):
        obra=lt.getElement(catalog["Obra"],i)
        if obra["DateAcquired"]!="":
           enfecha=dt.date.fromisoformat(obra["DateAcquired"])
           if enfecha>= fecha1 and enfecha<= fecha2:
               lt.addLast(artworksinrange, obra)
        i+=1
    sortlist=sortdate(artworksinrange)
    return sortlist

  #encontrar número de obras compradas
def purchaseart (listaordenada2):
    i=1
    n=0
    while i<=lt.size(listaordenada2):
        obra=lt.getElement(listaordenada2,i)
        if obra["CreditLine"]=="Purchase":
            n+=1
        i+=1
    return n
    
  # Funciones de ordenamiento
def sortdate (artworksinrange):
    sorted_list=mg.sort(artworksinrange, cmpArtworkByDateAcquired)
    return sorted_list

  # Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired (obra1, obra2):
    if obra1["DateAcquired"]!= "" and obra2["DateAcquired"]!= "":
        fecha1= dt.date.fromisoformat(obra1["DateAcquired"])
        fecha2= dt.date.fromisoformat(obra2["DateAcquired"])
        return fecha1<fecha2


#REQ. 3: clasificar las obras de un artista por técnica (Individual)
# Total de obras
def totalobrasartista (catalog, name):
    obras=lt.newList("ARRAY_LIST")
    for artista in lt.iterator(catalog["Artista"]):
        if artista["DisplayName"]== name:
            obras=artista["Artworks"]
    return obras

#Total técnicas (medios) utilizados
def totalmedios(obras):
    tecnicas=lt.newList("ARRAY_LIST", cmpfunction=cmpmediums)
    j=1
    while j <=lt.size(obras):
      obra=lt.getElement(obras,j)
      tecnica=obra["Medium"]
      posicion=lt.isPresent(tecnicas,tecnica)
      if posicion>0:
          tec=lt.getElement(tecnicas, posicion)
          tec["valor"]+=1
      else:
          tec={"Nombre":tecnica,"valor":1}
          lt.addLast(tecnicas, tec)
      j+=1
    sortedlist=sorttecnicas(tecnicas)
    return sortedlist

def sorttecnicas(tecnicas):
   sortedlist=mg.sort(tecnicas, cmptecnicas)
   return sortedlist

def cmptecnicas( tecnica1, tecnica2):
    if tecnica1["valor"]>=tecnica2["valor"]:
       return True
    else:
       return False
  
def cmpmediums (tecnica1,tecnica2):
  if tecnica1== tecnica2["Nombre"]:
    return 0
  else:
    return 1

#La técnica mas utilizada  
def primeratecnica (sortedlist):
   nombre=lt.firstElement(sortedlist)
   nombre=nombre["Nombre"]
   return nombre

#El listado de las obras de dicha técnica
def obrastecnica1(nombre,obras):
  listaobras=lt.newList("ARRAY_LIST")
  for obra in lt.iterator(obras):
    if obra["Medium"]==nombre:
      lt.addLast(listaobras,obra)
  return listaobras

#REQ. 4:clasificar las obras por la nacionalidad de sus creadores

def tomar (n, iterable):
  return list(islice(iterable,n))

def obrasRecurrentes (catalog , top):
  id = catalog["Artista"]
  lista= lt.newList(datastructure= "ARRAY_LIST")

  for artist in id.values():
    nacionalidad = artist["Nacionalidad"]
    if nacionalidad == top:
      for artwork in lt.iterator(artist["artworks"]):
        lt.addLast(lista, artwork)
  return lista

def diezNacionalidades (catalog):
  diccionario = {}
  identificacion = catalog["Artista"]

  for artist in identificacion.values():
    tamaño= lt.size(artist["artworks"])
    nacionalidad= artist["nacionalidad"]

    if nacionalidad != "" or nacionalidad != "Nationality unknown":
      if nacionalidad not in diccionario.keys():
        diccionario[nacionalidad]= tamaño
      else:
        diccionario[nacionalidad]+= tamaño

  organizado= dict(sorted(diccionario.items(),key=lambda item:item[1], reverse= True))

  nacionalidades= tomar(100, organizado.items())
  primera= nacionalidades[0][0]
  lista= obrasRecurrentes(catalog, primera)
    
  return nacionalidades, lista

def obrastecnica (nombre,obras):
  listaobras=lt.newList("ARRAY_LIST")
  for obra in lt.iterator(obras):
    if obra["Medium"]==nombre:
      lt.addLast(listaobras,obra)
  return listaobras
  


#REQ. 5: transportar obras de un departamento
#Total de obras para transportar (size de esto)
def totalobras(catalog, depto):
   listaobras= lt.newList("ARRAY_LIST")
   obras=catalog["Obra"]
   for obra in lt.iterator(obras):
     if obra["Department"]==depto:
       lt.addLast(listaobras,obra)
   return listaobras

#Estimado en USD del precio del servicio
def price (listaobras):
    totalprice=0
    costo=72
    for obra in lt.iterator(listaobras):
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
       weight=obra["Weight"]
       diameter=obra["Diameter"]
       circumference=obra["Circumference"]
       length=obra["Length"]
       height=obra["Height"]
       width=obra["Width"]
       depth=obra["Depth"]
       if weight !="" :
         kgprice=float(weight)*costo
       if height!= "" and width!= "":
         m2price1=(float(height)/100)*(float(width)/100)*costo
       if height!= "" and length!= "":
         m2price2=(float(height)/100)*(float(length)/100)*costo
       if height!= "" and depth!= "":
         m2price3=(float(height)/100)*(float(depth)/100)*costo
       if length!= "" and width != "":
         m2price4= (float(length)/100)*(float(width)/100)*costo
       if depth!="" and width!="":
         m2price5= (float(depth)/100)*(float(width)/100)*costo
       if length!="" and depth!="":
         m2price6= (float(length)/100)*(float(depth)/100)*costo
       if diameter !="":
         m2price8=3.1416*(((float(diameter)/2)/100)**2)*costo
       if circumference!="":
         m2price9= 3.1416*(((float(circumference)/100)/(2*3.1416))**2)*costo

       if length!="" and width != "" and depth != "":
         m3price1=(float(length)/100)*(float(width)/100)*(float(depth)/100)*costo
       if height!="" and width!= "" and depth!= "":
         m3price2=(float(height)/100)*(float(width)/100)*(float(depth)/100)*costo
       if height!="" and width!= "" and length!= "":
         m3price3=(float(height)/100)*(float(width)/100)*(float(length)/100)*costo
       if length!="" and depth!= "" and height!= "":
         m3price4=(float(length)/100)*(float(depth)/100)*(float(height)/100)*costo
       if height!="" and diameter!= "":
         m3price5=3.1416*((((float(diameter))/2)/100)**2)*(float(height)/100)*costo
       if width!="" and diameter!="":
         m3price6=3.1416*((((float(diameter))/2)/100)**2)*(float(width)/100)*costo
       if depth!="" and diameter!="":
         m3price7=3.1416*((((float(diameter))/2)/100)**2)*(float(depth)/100)*costo
       if length!="" and diameter!="":
         m3price8=3.1416*((((float(diameter))/2)/100)**2)*(float(length)/100)*costo
       lastprice= max(kgprice,m2price1,m2price2,m2price3,m2price4,m2price5,m2price6,m2price7,m2price8,m2price9,m3price1,m3price2,m3price3,m3price4,m3price5,m3price6,m3price7,m3price8)
       if lastprice==0:
         lastprice=48
       obra["Price"]=lastprice
       totalprice+=lastprice
    return (totalprice, listaobras)

#Peso estimado de las obras
def weight (listaobras):
  peso=0
  for obra in lt.iterator(listaobras):
    pes=obra["Weight"]
    if pes== "":
      peso+=0
    else:
      pesinfloat=float(pes)
      peso+=pesinfloat
  return peso

#Obras viejas
def oldest (listaobras):
  sortedlist=sortviejas(listaobras)
  return sortedlist

def sortviejas (listaobras):
  sorted_list=mg.sort(listaobras, cmpmasvieja)
  return sorted_list

def cmpmasvieja(fecha1, fecha2):
  if fecha1["Date"]!="" and fecha2["Date"]!="":
    date1=int(fecha1["Date"])
    date2=int(fecha2["Date"])
    return date1>date2

#mas costosas
def expensive(listaobras):
  sortlist=sortcaras(listaobras)
  return sortlist

def sortcaras(listaobras):
  sort_list=mg.sort(listaobras, cmpmascara)
  return sort_list

def cmpmascara(precio1,precio2):
  price1=precio1["Price"]
  price2=precio2["Price"]
  return price1>price2
# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
