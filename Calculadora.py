def suma(num1, num2):
    return num1 + num2

# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu():
    print("Calculadora Básica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    opcion = input("Elige una opción (1-5): ")
    return opcion

# Función principal del programa
def main():
    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = suma(num1, num2)
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == '2':
            # Implementa la lógica para la resta
            pass
        elif opcion == '3':
            # Implementa la lógica para la multiplicación
            pass
        elif opcion == '4':
            # Implementa la lógica para la división
            pass
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor elige una opción del 1 al 5.")

if __name__ == "__main__":
    main()