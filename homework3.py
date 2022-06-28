import os
archivo=open("Emisiones_CO2.csv","r")
dicc_emisiones={}
#Obtengo primera fila
titulos=archivo.readline()
keys=titulos.split("|")
keys=tuple(keys)


#Utilizo primera fila como keys del diccionario
for elements in keys:
    dicc_emisiones[elements]=[]


print(dicc_emisiones)



#Carga del csv
filas=archivo.readlines(0) 


#iterar y separar | 

i=0

for fila in filas:
    dato=fila.split("|")
    if i==0:
        pass
    else:
        dicc_emisiones['cod_pais'].append(dato[0])
        dicc_emisiones['nom_pais'].append(dato[1])
        dicc_emisiones['region'].append(dato[2])
        dicc_emisiones['anio'].append(dato[3])
        dicc_emisiones['co2'].append(dato[4])
        dicc_emisiones['co2_percapita'].append(dato[5])

    i+=1


