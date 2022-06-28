import os
archivo=open("Emisiones_CO2.csv","r")
dir={}
#Obtengo primera fila
titulos=archivo.readline()
keys=titulos.split("|")
keys=tuple(keys)


#Utilizo primera fila como keys del diccionario
for elements in keys:
    dir[elements]=[]





dicc_emisiones = {  'cod_pais' : [],
                    'nom_pais' : [],
                    'region' : [],
                    'anio' : [],
                    'co2' : [],
                    'co2_percapita' : []}

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


print(len(dicc_emisiones))
#6

print(type(dicc_emisiones['cod_pais']))
#cod 


#e) ¿Cuál es el total de emisiones de CO2 para 'América Latina y Caribe' en el año 2010?

dicc_emisiones["region"]

filtro_region = 'América Latina y Caribe'
filtro_anio = '2010'
emisiones = 0
for indice, elemento in enumerate(dicc_emisiones['region']):
    if (dicc_emisiones['region'][indice] == filtro_region):
        if (dicc_emisiones['anio'][indice] == filtro_anio):
            if (dicc_emisiones['co2'][indice] != None):
                emisiones += dicc_emisiones['co2'][indice]
print('Las emisiones en', filtro_region, 'en', filtro_anio, 'fueron de',emisiones,'kt')