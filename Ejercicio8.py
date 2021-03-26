#Pregunta 8:
 
#Escribir un programa que tenga como input 10 numeros positivos de 3 digitos,
# y como output liste los que son capicuas,
 
#ordenandolos de menor a mayor

def capicuas(lista):

    capicuas = [] #lista vacia para almecenar capicuas
    
    for num in lista: # recorremos la lista
        count = 1 
        for n in str(num):
            if count == 1: # primer digito
                digito1 = n
            elif count == 3: # tercer digito
                digito3 = n
    
            count += 1 # contabilizamos el numero de digito
        
        if digito1 == digito3: #si el primer digito y el tercer digito son iguales
            capicuas.append(num)
    
    return capicuas


lista = [234, 191, 157, 389, 757, 834, 331, 642, 404, 519]

print(capicuas(lista)) # 191, 757, 404
