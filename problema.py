# input("") permite al usuario ingresar un valor por consola
# Consigna,
# A partir de un string ingresado por consola
# determinar si dicho string es palindromo
# Palindromo: alreves y normal se escriben igual, neuquen, jojo
#cadena = input("Ingrese una cadena de texto: ")
#print("Esta es una cadena:", cadena)

def es_palindromo(texto):
    # Comparar el texto con su reverso
    return texto == texto[::-1]

# Función para solicitar input al usuario y verificar si es palíndromo
def verificar_palindromo():
    texto = input("Ingresa una palabra para verificar si es palíndromo: ")
    if es_palindromo(texto):
        print(f"'{texto}' es un palíndromo.")
    else:
        print(f"'{texto}' no es un palíndromo.")

# Ejecutar la función para verificar palíndromo
verificar_palindromo()