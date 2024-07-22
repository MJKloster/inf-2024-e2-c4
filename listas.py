from functools import reduce

lista = [1, 2, 3, 4, 5]

suma = sum(lista)
longitud = len(lista)
maximo = max(lista)
minimo = min(lista)
ordenar = sorted(lista)
reversa = list(reversed(lista)) # lista[::-1]
enumerar = list(enumerate(lista))
mapear = list(map(lambda x: x + 3, lista))
mapRed = reduce(lambda x, y: x + y, lista)
filtrado = list(filter(lambda x: x % 2 == 0, lista))


print("Suma: ", suma)
print("Longitud: ", longitud)
print("Maximo: ", maximo)
print("Minimo: ", minimo)
print("Ordenado: ", ordenar)
print("Reversa: ", reversa)
print("Enumerar: ", enumerar)
print("mapear: ", mapear)
print("mapRed: ", mapRed)
print("Filtrado: ", filtrado)