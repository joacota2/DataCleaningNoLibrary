import os
import csv
"""archivo = open('Emisiones_CO2.csv', 'r')

#Columna 0 en formato str
titulos=archivo.readline()

#Lista de llaves (fila 0) en formato lista
data=[]
keys=titulos.split("|")


print(keys)

#Numero total de filas
cuenta=len(archivo.readlines())
print(cuenta)
"""

with open('Emisiones_CO2.csv',mode='r') as archivo:
    data=[]
    data2=[]
    reader=csv.reader(archivo)

    #str de primera fila
    titulos=archivo.readline()

    #list de primera fila
    keys=titulos.split("|")
    print(keys)

    #csv en formato de lista
    filas=archivo.readlines()
    for elementos in filas:
        data.append(elementos)
        for i in data



