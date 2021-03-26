# Pregunta 7:
 
#Desarrollar una funcion que me devuelva el n-esimo fibonacci
#Recordar que la serie fibonacci inicia en uno, es decir que fibonacci(1) = 1, ademas que
 
#El fibonacci(3) = fibonacci(2) + fibonacci(1)
 
#Nota: Implementarlo de modo iterativo.

def fibonacci(n):

    num1, num2 = 0, 1 # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
    for i in(range(n-1)):
        temp = num2  # se reserva el valor del segundo número
        num2 += num1 # al segundo número se le suma el primer número
        num1 = temp # ahora el primer número se convierte en el segundo número
    
    if n > 0: return num2 # si el valor entrante es mayor a 0
    else: return 0


numero = 9 #34
print(fibonacci(numero)) # Vemos el fibonnacci de un respectivo número
