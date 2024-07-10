
nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))


promedio = (nota1 + nota2 + nota3) / 3
print(f"El promedio es: {promedio}")

if promedio >= 65:
    print("Aprobó")
else:
    print("Reprobó")
