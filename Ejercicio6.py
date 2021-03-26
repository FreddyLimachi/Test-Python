# Ejercicio 6

# Crear una funcion que determine si dado una serie de parentesis, 
# estas se encuentran en pares, es decir,
 
#abierto '(' y cerrado ')'.
 
#Ejm:
 
 #Entrada: '(()()())()()(())'
 #Salida: True
 
 #Entrada: '(()('
 #Salida: False

def ParImpar(string):

    abierto, cerrado = 0, 0 # inicializamos numero de parentesis en 0

    for i in string:
        if i == "(": abierto += 1
        else: cerrado += 1
    
    if abierto == cerrado: return True

    else: return False
        
string1 = "(()()())()()(())"

string2 = "(()("

print(ParImpar(string1)) # True

print(ParImpar(string2)) # False
