# Pregunta 8:
 
# Desarrollar un programa que encuentre el 20avo numero capicúa de 3 digitos

def capicua():
    
    count = 0 #conteo de capicuas
    numero = 100 #empezamos con 3 digitos

    while count < 20: #hasta encontrar el 20avo capicua

        lista_num = list(str(numero)) # separamos digitos en una lista

        if lista_num == lista_num[::-1]: #invertimos la lista
            capicua=''.join(lista_num) #juntar los numeros de la lista
            count += 1 # incrementando el contador
        
        numero += 1 #incrementamos el numero para la prueba           
            
    print("El 20vo capicúa de 3 dígitos es: ", capicua)

capicua()