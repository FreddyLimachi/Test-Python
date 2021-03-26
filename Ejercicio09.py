#Pregunta 9:
 
# Hacer un programa que genere un array y que imprima los numeros que no son iguales

from random import randint

def Generar():
    
    lista = [] # inicializar una lista vacia

    for num in range(10): # recorrer 10 elementos
        lista.append(randint(0,10)) # generar números entre 0 a 10

    print(lista) # ver la lista generada de números
    
    NoIguales = [] # Lista vacia de numeros que no se repiten
    
    for i in lista:
        count = 0 # reiniciar contador en 0

        for j in lista:
            
            if i==j: 
                count += 1 # incremento de contador cada vez que encuentra números iguales 
            
        if count == 1: # si el contador solo encontro un numero igual (el mismo)
            NoIguales.append(i)

    print(NoIguales) # ver los números que no se repiten
                
Generar() # Ejecutar la función
