# Pregunta 5:
 
# Escribir una funcion sum() y una función multip() que sumen y 
# multipliquen respectivamente todos los números de una lista.

def sum(lista):
    suma = 0 # la suma inicializa en 0
    for num in lista:
        suma += num # suma de los numeros de la lista
    
    return suma

def multip(lista):
    producto = 1 # el producto inicializa en 1
    for num in lista:
        producto *= num # producto de los numeros de la lista
    
    return producto


lista = [2,6,4,15,7] # lista de numeros

print(sum(lista)) # Ver la suma total

print(multip(lista)) # Ver el producto total
