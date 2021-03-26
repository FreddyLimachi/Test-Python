# Ejercicio 6

# Crear una funcion que determine si dado una serie de parentesis, 
# estas se encuentran en pares, es decir,
 
#abierto '(' y cerrado ')'.
 
#Ejm:
 
#Entrada: '(()()())()()(())'
#Salida: True

#Entrada: '(()('
#Salida: False

def balanceo(string):

    pila = [] # definir nuestra lista
    parentesis = {'(':')'} # definir clave valor de "(" = ")"

    for i in string: # recorrer el string
        if i in parentesis: # si el caracter se encuentra en nuestro diccionario
            pila.append(i) 
        elif len(pila) == 0 or i != parentesis[pila.pop()]: # si la pila esta vácia o el 
            return False                                    # caracter es diferente al parentesis
                                                            # de cierre del ultimo elemento de la lista
    
    if len(pila) == 0: return True # si la pila esta vacía
    else: return False
  

string1 = "(()())()"
string2 = ")(()"

print(balanceo(string1)) # True
print(balanceo(string2)) # False
