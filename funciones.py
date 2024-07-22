print("Bienvenido")
seguir = "SI"
while seguir == "SI":
    print ("Elija una opción:  ")
    print ("1-SUMA")
    print ("2-RESTA")
    print ("3-DIVIDIR")
    print ("4-MULTIPLICAR")
    print ("0-SALIR")
    oper= int(input())

    if oper == 0:
        seguir= "NO"
        print("¡Hasta luego!")
        break
    elif oper >= 5:
        print ("La opcion elegida no corresponde a ningun Operador") 
        seguir = "SI";        
    else:
        num1 = int(input("Ingrese el primer numero: ")) 
        num2 = int(input("ingrese el segundo numero: "))

        if oper == 1:
            resultado = num1 + num2
        elif oper == 2:
            resultado = num1 - num2
        elif oper == 3:
            resultado = num1 // num2
        elif oper == 4:
            resultado = num1 * num2
        else:
            resultado = 0
        print (f"El resultado es: {resultado}")
        seguir= input ("seguimos? SI/NO\n: ").upper()

#print("Gracias por usar nuestra calculadora")