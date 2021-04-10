import glob
import os
import filecmp

def archivos_repetidos(ruta):

    files = glob.glob(ruta + os.path.sep + "*") # leer todos los archivos y carpetas

    print("\nLista de todos los archivos")
    print("================================================================")
    for file in files:
        size = os.path.getsize(file) #obteniendo tamaño
        print(file.replace(ruta, "/"), "\t\t " , size,"bytes")  #rutas relativas
    
    duplicados = []
    nro_duplicados = 0
    sum_bytes_duplicados = 0

    for i in range(len(files)):
        for j in range(i+1,len(files)): #recorrer a partir del siguiente elemento de la primera iteracion
            
            result = filecmp.cmp(files[i], files[j], shallow=True) # comparando archivos en contenido

            if result: # si se obtiene True
                size = os.path.getsize(files[j]) #obtener tamaño del archivo
                sum_bytes_duplicados += size # sumar tamaños de los duplicados
                nro_duplicados += 1 # sumar los archivos que se repiten
                duplicados.append(files[j].replace(ruta, "/")+"\t\t"+str(size)+" bytes") #agregar a la lista los duplicados
    

    print("\n================================================================")
    print("Número de archivos repetidos: ", nro_duplicados)
    print("Suma en bytes de archivos repetidos: ", sum_bytes_duplicados)
    print("\n================================================================")
    print("ARCHIVOS DUPLICADOS")
    for file in duplicados:
        print(file)

ruta = input("Digite la ruta: ") # ruta absoluta
archivos_repetidos(ruta)
