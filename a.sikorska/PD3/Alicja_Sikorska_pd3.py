# Zadanie 1

def Ciag_fib(n):
    a = 1
    b = 1
    print(a)
    print(b)
    for i in range(1, n-1):
        a, b = b, a + b
        print(b)
    return

Ciag_fib(50)

# Zadanie 3

def Unique_elements(*lista):
    lista_unique=[]
    for n in range(0, len(lista)) :
        if lista[n] not in lista_unique :
            lista_unique.append(lista[n])   
    print(lista_unique)
    return

Unique_elements(1,2,3,3,3,3,4,5)
