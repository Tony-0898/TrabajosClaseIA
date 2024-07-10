
distancia = float(input("Ingresa la distancia en metros: "))
tiempo = float(input("Ingresa el tiempo en segundos: "))

# velocidad (V = d/t)
if tiempo != 0:
    velocidad = distancia / tiempo
    print(f"La velocidad del automóvil es {velocidad} metros por segundo.")
else:
    print("El tiempo no puede ser cero.")
