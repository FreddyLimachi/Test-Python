
#Pregunta 2:

#Escribir un codigo en python que sume y multiplique 
#respectivamente todos los numeros de una lista, ejemplo;

# Numeros=1 2 3 4, suma 10, multiplicacion 24.

def Operar(lista):

    suma, producto = 0, 1 # inicializando en neutro la suma y el producto
    for num in lista:
        suma += num # suma de los numeros
        producto *= num # producto de los numeros
    
    print("Suma: ", suma ,", Multiplicación: ", producto)
    
lista = [1,2,3,4] #lista de numeros

Operar(lista) # Ejecutamos la funcion Operar

