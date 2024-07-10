numero = int(input("Ingresa un número entre 0 y 10: "))

if 0 <= numero <= 10:
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")
else:
    print("El número ingresado no está entre 0 y 10.")
