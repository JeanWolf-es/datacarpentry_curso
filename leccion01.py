#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:48:53 2020

@author: jeanwolf
Leyendo datos en CSV usando Pandas

https://datacarpentry.org/python-ecology-lesson-es/02-starting-with-data/index.html

"""
import pandas as pd
import os

# el parametro dtypes es ver que tipo de dato tiene cada columna
surveys_df = pd.read_csv("data/surveys.csv")
print(surveys_df)   
p = surveys_df.dtypes

# el parametro colums es ver el header de cada columna
q = surveys_df.columns
surveys_df.dtypes.to_csv("data/dtypes.csv")

# mostrar solo el header mediante el metodo for
for column in surveys_df:
    print(column)

# Aqui se escribe los parametros en archivos txt
txt01 = open("data/txt/dtypes.txt","w")
txt02 = open("data/txt/headers.txt","w")
# para escribir en el archivo de texto una variable se usa str 
txt01.write(str((p)))
txt02.write(str((q)))
txt01.close()
txt02.close()

"""
ejercicio.
con el DataFrame surveys_df, ejecuta los atributos y métodos siguientes y observa que regresan.

    surveys_df.columns
    surveys_df.shape
        Toma nota de la salida deshape


    Sugerencia: Más acerca de tuplas, aquí.
    surveys_df.head()
    También ejecuta
    surveys_df.head(15) ¿qué hace esto?
    surveys_df.tail()
"""

# 1.
# muestra el numero de entradas y campos
print(surveys_df.shape)

# la funcion .head toma x entradas incluyendo el header
# x puede es un numero integro
r = surveys_df.head(25)
txt03 = open("data/txt/head.txt","w")
txt03.write(str((r)))
txt03.close()

# Estadisticas
# describe == las estadisticas basicas de la columna
# en este caso se toma la columna weight
surveys_df['weight'].describe()
# para el caso de la columna hindfoot_length
surveys_df['hindfoot_length'].describe()

# extraer una medida en particular
surveys_df['weight'].min()

surveys_df['weight'].max()
surveys_df['year'].mean()
surveys_df['weight'].std()
surveys_df['hindfoot_length'].count()
print("+++++++++++++++++++++")

"""
### .groupby vs .describe ###
.describe == regresa valores de estadísticas para las columnas numéricas
.groupby == regresa estadisticas por el grupo de nuestra elección.
.groupby == requiere que se genere un DataFrame especifico
.groupby permite sacar estadisicas de una columna en funcion de las demas.
por ejemplo. sacar la media de la columna SEX, de las columnas 
record_id     month        day  ...    plot_id  hindfoot_length     weight

"""
# paso 1: crear el DataFrame. en este caso con una variable especifica
grouped_data = surveys_df.groupby('sex')

# paso 2: sacar la media por el conjunto de datos
t = grouped_data.count()
txt04 = open("data/txt/grouped_data.txt","w")
txt04.write(str((t)))
txt04.close()


# ejercicio: ¿Cuántos individuos son hembras F y cuántos son machos M?
c = grouped_data.count()
txt05 = open("data/txt/grouped_count.txt","w")
txt05.write(str((c)))
txt05.close()

# respuesta: 
# F        15690
# M        17348

# Ejercicio:
# Describe lo ocurrido cuando se agrupa dos columnas y se toma medidas
grouped_data2 = surveys_df.groupby(["weight","sex"])
grouped_data2.count().to_csv("data/grouped_mean.csv")
# respuesta:
# en el caso de weight y sex agrupa las colunas y muestra estadisticas de las
# agrupaciones. Por ejemplo. para el caso de un peso de 18 Kg
# weight	sex	record_id	month	day	year	plot_id	hindfoot_length
# 18.0	F	23353.291803278687	7.101639344262295	16.74098360655738	1994.5901639344263	10.852459016393443	21.51689189189189
# 18.0	M	23006.204946996466	6.763250883392226	16.402826855123674	1994.303886925795	12.049469964664311	21.6
# indica que el promedio de captura esta en en julio de 1994. y el tamaño de su pata es de 21,5 para Hembras y 21,6 para Machos

# ejerccio: hallar la cantidad de machos y hembras por sitio y el promedio de peso

grouped_data3 = surveys_df.groupby(["plot_id","sex"])
grouped_data3.count().to_csv("data/ejer/grouped_count_sex.csv")

grouped_data4 = surveys_df.groupby(["sex", "plot_id"])
grouped_data4.mean().to_csv("data/ejer/grouped_mean_sex.csv")

# ejercicio: Calcula las estadísticas descriptivas del peso para cada sitio.

grouped_data5 = surveys_df.groupby(["plot_id", "sex"])
grouped_data5.describe().to_csv("data/ejer/grouped_describe.csv")



print("FIN DEL CALCULO del EJERCICIO")

