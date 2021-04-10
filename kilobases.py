import random

def kilobases():

    err = True
    while err == True:
        try:
            cantidad_kb= int(input("Digite una cantidad de kilobases de ADN: "))
            err = False
        except ValueError:
            err = True

    try:
        GC = float(input("Digite un porcentaje de pares GC en decimales (0 - 1): "))
        if GC < 0 or GC > 1:
              GC = 0.5

    except ValueError:
        GC = 0.5

    A,T,G,C = "A","T","G","C"

    total_GC = round(cantidad_kb*GC)
  
    G = G * random.randint(0,round(total_GC))
    C = C * (total_GC - len(G))

    total_AT = cantidad_kb - total_GC

    A = A * random.randint(0,round(total_AT))
    T = T * (total_AT - len(A))

    lista = list(A+T+G+C)
    
    random.shuffle(lista)

    secuencia = ''.join(lista)

    print(secuencia)


kilobases()
    