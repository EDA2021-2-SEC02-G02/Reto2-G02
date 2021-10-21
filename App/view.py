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


from model import totalartworks
import config as cf
import sys
import controller
import time as time
from DISClib.ADT import list as lt
assert cf

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("0- Cargar información en el catálogo")
    print("1- Listar cronologicamente los artistas")
    print("2- Listar cronologicamente las adquisiciones")
    print("3- Clasificar obras de un artista por técnica")
    print("4- Clasificar las obras por nacionalidad de sus creadores")
    print("5- Transportar obras de un departamento")


def inicializar_catalogo():
    return controller.initcatalog()

def cargarinfo(catalog):
    controller.loaddata(catalog)

catalog=None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

#Carga de datos
    if int(inputs[0]) == 0:
        start_time = time.perf_counter()
        print("Cargando información de los archivos ....")
        catalog=inicializar_catalogo()
        cargarinfo(catalog)
        print("Artistas cargados "+str(lt.size(catalog["Artist"])))
        print("Obras cargadas "+str(lt.size(catalog["Artwork"])))
        stop_time = time.perf_counter()
        delta_time = (stop_time - start_time)*10000
        print(delta_time)

    elif int(inputs[0]) == 1:
        year1= int(input("Ingrese el año inicial del que desea organizar los artistas: "))
        year2= int(input("Ingrese el año final del que desea organizar los artistas: "))
        start_time = time.perf_counter()
        print("Buscando....")
        list1=controller.addartistyear(catalog, year1, year2)
        nartists=lt.size(list1)
        print("El número total de artistas en dicho rango es de: "+ str(nartists))
        print(" los 3 primeros artistas del rango cronológico  son: ")
        threefirst1=(lt.getElement(list1,1),lt.getElement(list1,2),lt.getElement(list1,3))
        for artistF in threefirst1:
            print("Nombre: "+artistF["DisplayName"]+
                  ". Fecha de nacimiento: " +artistF["BeginDate"]+
                  ". Fecha de fallecimiento: " +artistF["EndDate"]+
                  ". Nacionalidad: " +artistF["Nationality"]+
                  ". Género: " +artistF["Gender"])
        print("los 3 últimos artistas del rango cronológico (nombre, año de nacimiento, año de fallecimiento, nacionalidad y género) son: ")
        threelast1=(lt.getElement(list1,nartists) ,lt.getElement(list1,nartists-1),lt.getElement(list1,nartists-2))
        for artistL in threelast1:
            print("Nombre: "+artistL["DisplayName"]+
                  ". Fecha de nacimiento: " +artistL["BeginDate"]+
                  ". Fecha de fallecimiento: " +artistL["EndDate"]+
                  ". Nacionalidad: " +artistL["Nationality"]+
                  ". Género: " +artistL["Gender"])
        stop_time = time.perf_counter()
        delta_time = (stop_time - start_time)*10000
        print(delta_time)

    elif int(inputs[0]) == 2:
        date1= input("Ingrese la fecha inicial (AAAA MM DD): ")
        date2= input("Ingrese la fecha final (AAAA MM DD): ")
        start_time = time.perf_counter()
        print("Creando lista ....")
        list2= controller.addartworkyear(catalog, date1, date2)
        Npurchaseartworks=controller.purchaseart(list2)
        size=lt.size(list2)
        print("El número total de obras en el rango cronológico es de: "+ str(size))
        print("El número total de obras adquiridas por compra es de: "+str(Npurchaseartworks))
        print("Las tres primeras obras del rango cronológico son: ") 
        threefirst2= (lt.getElement(list2,1),lt.getElement(list2,2),lt.getElement(list2,3))
        for artworkF in threefirst2:
            print("Título: "+artworkF["Title"]+ 
                  ". Fecha: "+artworkF["Date"]+
                  ". Medio: " +artworkF["Medium"]+
                  ". Dimensiones: " +artworkF["Dimensions"])
            print("Los artistas de la obra son: ")
            for artist in lt.iterator(artworkF["Artists"]):
                print(artist["DisplayName"])
        print("Las tres últimas obras del rango cronológico son: " )
        threelast2=(lt.getElement(list2,size),lt.getElement(list2,size-1),lt.getElement(list2,size-2))
        for artworkL in threelast2:
            print("Título: "+artworkL["Title"]+
                  ". Fecha: "+artworkL["Date"]+
                  ". Medio: " +artworkL["Medium"]+
                  ". Dimensiones:" +artworkL["Dimensions"])
            print("Los artistas de la obra son: ")
            for artist in lt.iterator(artworkF["Artists"]):
                print(artist["DisplayName"])
        stop_time = time.perf_counter()
        delta_time = (stop_time - start_time)*10000
        print(delta_time)
        
    elif int(inputs[0]) == 3:
        name=input("Ingrese el nombre del artista: ")
        start_time = time.perf_counter()
        totalartworkss=controller.totalartworksartist(catalog, name)
        totalo=lt.size(totalartworkss)
        if totalo==0:
            print("El artista no tiene obras")
        else:
           totalmedium=controller.totalmediums(totalartworkss)
           totalm=lt.size(totalmedium)
           nametec=controller.firsttechnique(totalmedium)
           listtec=controller.artworkstechnique1(nametec,totalartworkss)
           print("El total de las obras del artista "+name+" es de: "+str(totalo))
           print("El total de tecnicas utilizadas es de: "+str(totalm))
           print("Las técnicas más utilizada por el artista son: ")
           fivefirst=(lt.getElement(totalmedium,1), lt.getElement(totalmedium,2), lt.getElement(totalmedium,3), lt.getElement(totalmedium,4), lt.getElement(totalmedium,5))
           for medium in fivefirst:
               print (medium["Name"],medium["value"])           
           print("El listado de las obras de dicha técnica es: ")
           threefirst=(lt.getElement(listtec,1), lt.getElement(listtec,2), lt.getElement(listtec,3))
           for artwork in threefirst:
              print("Titulo: "+artwork["Title"]+
                    ". Fecha: "+artwork["Date"]+
                    ". Medio: "+artwork["Medium"]+
                    ". Dimension:"+artwork["Dimensions"])
        stop_time = time.perf_counter()
        delta_time = (stop_time - start_time)*10000
        print(delta_time)
        


    elif int(inputs[0])== 4:
        result= controller.clasifyByNationality(catalog)
        start_time = time.perf_counter()

        print("TOP 10 NACIONALIDADES EN EL MOMA:")
        
        
        if lt.size(result) >= 10:
            for i in range(1,11):
                a=lt.getElement(result,i)
                print(a["nacionalidad"],lt.size(a["obras"]))
        else: 
            for i in range(1,lt.size(result)+1):
                a=lt.getElement(result,i)
                print(a["nacionalidad"],lt.size(a["obras"]))


        print("PRIMEROS 3")
        #primeros 3
        mayorNacionalidad=lt.firstElement(result)
        for  i in range(1,4):
            a=lt.getElement(mayorNacionalidad["obras"],i)
            print("\nTITULO DE LA OBRA:",a["Title"])
            print("\nFECHA DE LA OBRA:",a["Date"])
            print("\nMEDIO DE LA OBRA:",a["Medium"])
            print("DIMENSIONES DE LA OBRA:",a["Dimensions"])
            print("\n")

        print("ULTIMOS 3")
        #ultimos 3
        for i in range(lt.size(mayorNacionalidad["obras"])-2,lt.size(mayorNacionalidad["obras"])+1):
            a=lt.getElement(mayorNacionalidad["obras"],i)
            print("\nTITULO DE LA OBRA:",a["Title"])
            print("\nFECHA DE LA OBRA:",a["Date"])
            print("\nMEDIO DE LA OBRA:",a["Medium"])
            print("\nDIMENSIONES DE LA OBRA:",a["Dimensions"])
            print("\n")

        

        stop_time = time.perf_counter()
        delta_time = (stop_time - start_time)*10000
        print(delta_time)

    elif int(inputs[0])== 5:
       depto=input("Ingrese el departamento del museo que desea transportar: ")
       start_time = time.perf_counter()
       listartworks=controller.totalartworks(catalog, depto)
       totalart=lt.size(listartworks)
       price=controller.price(listartworks)
       priceart=price[0]
       weight=controller.weight(listartworks)
       listoldest=controller.oldest(listartworks)
       print("El total de obras para transportar es de: "+str(totalart))
       print("El estimado en USD del precio del servicio es de: "+str(priceart))
       print("El peso estimado de las obras a transportar es de: "+str(weight))
       oldest=controller.oldest(price[1])
       listexpensive1=price[1]
       fiveoldest=(lt.getElement(oldest,1),lt.getElement(oldest,2), lt.getElement(oldest,3), lt.getElement(oldest,4), lt.getElement(oldest,5))
       print("Las 5 obras más antiguas a transportar son: ")
       for artwork in fiveoldest:
            print("Titulo: "+artwork["Title"]+
                 ". Clasificación: " +artwork["Classification"]+
                 ". Fecha: " +artwork["Date"]+
                 ". Medio: " +artwork["Medium"]+
                 ". Dimensiones: " +artwork["Dimensions"]+ 
                 ". Costo asociado al transporte: "+str(artwork["Price"]))
            print("El/los artista(s) de la obra son: ")
            for artist in lt.iterator(artwork["Artists"]):
                print(artist["DisplayName"])
       listexpensive=controller.expensive(listexpensive1)
       fiveexpensive=(lt.getElement(listexpensive,1), lt.getElement(listexpensive,2),lt.getElement(listexpensive,3), lt.getElement(listexpensive,4), lt.getElement(listexpensive,5))
       print("Las 5 obras más antiguas a transportar son :" )
       for obra in fiveexpensive:
            print("Titulo: "+artwork["Title"]+
                 ". Clasificación: " +artwork["Classification"]+
                 ". Fecha: " +artwork["Date"]+
                 ". Medio: " +artwork["Medium"]+
                 ". Dimensiones: " +artwork["Dimensions"]+ 
                 ". Costo asociado al transporte: "+str(artwork["Price"]))
            print("El/los artista(s) de la obra son: ")
            for artist in lt.iterator(artwork["Artists"]):
                print(artist["DisplayName"])
       stop_time = time.perf_counter()
       delta_time = (stop_time - start_time)*10000
       print(delta_time)

    else:
        sys.exit(0)


