# Pregunta 1:

# Generar un codigo en python que sume 10 numeros aleatorios de la siguiente forma:
# los 5 mas bajos y los 5 mas altos

from random import randint

def ordenar(lista): #funcion para ordenar una lista de numeros

    for i in range(0, len(lista)-1):
        min = i # valor minimo empieza en la primera iteración
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min]: # intercambiamos elementos de la lista
                temp = lista[j]
                lista[j] = lista[min]
                lista[min] = temp   

    return lista

def suma():

    lista = []
    for i in range(10): #Generamos una lista aletoria de 10 numeros
        lista.append(randint(0,100))  #rango 0 a 100
    
    print(lista) # ver la lista generada

    lista = ordenar(lista) # Generamos la lista ordenada
    count = 0 # contador
    suma_menores, suma_mayores = 0, 0 
     
    for num in lista:
        if count < 5: # separar la lista por mitad
            suma_menores += num
        else: suma_mayores += num
        
        count += 1
    
    print("suma de los 5 numeros menores: ", suma_menores)
    print("suma de los 5 numeros mayores: ", suma_mayores)
    
suma() #Ejecutamos la funcion suma
    