# Sumar todos los valores del siguiente lista/array e imprimirlos por pantalla
lista = [1,2,3,4,5]

def sumar_lista(lista):
    suma=0
    for numero in lista:
        suma += numero
    return suma    
resultado = sumar_lista(lista)
print(resultado);