# Pregunta 4:
 
# Hacer un programa que tenga la funcion de listar las carpetas y
# archivos y ordenar por tamaño o fecha, y que muestre
 
# si hay archivos duplicados en contenido

import glob
import os
import filecmp

ruta = input("Digite la ruta: ") # ruta absoluta

files = glob.glob(ruta + os.path.sep + "*") # leer todos los archivos y carpetas

files.sort(key=os.path.getctime) # orderar los archivos por fecha de creación

for file in files: # Listando los archivos y carpetas ordenados por fecha de creación
    print(file)

print("===============================================================================")
print("\nLos siguientes archivos son repetidos en contenido:")

for i in files:
    for j in files:
        if i != j: # no comparar archivos consigo mismo
            result = filecmp.cmp(i, j, shallow=True) # comparando archivos en contenido

            if result: # si se obtiene True
                print(j)

