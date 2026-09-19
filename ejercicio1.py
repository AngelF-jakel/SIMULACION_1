
def generar_icg(semilla: int, cantidad: int,
                 p: int = 1009,   
                 a: int = 11,
                 c: int = 12):
    
  
    if not (0 <= semilla < p):
        raise ValueError(f"La semilla debe estar en el rango [0, {p - 1}]")
    if cantidad < 0:
        raise ValueError("La cantidad de valores a generar no puede ser negativa")

    def inverso_modular(x, modulo):
        # Por convencion en el ICG, el inverso de 0 se define como 0
        if x == 0:
            return 0
        return pow(x, modulo - 2, modulo)  # valido porque 'modulo' es primo
  


    resultados = []
    x = semilla
    for _ in range(cantidad):
        x = (a * inverso_modular(x, p) + c) % p
        resultados.append(x)

    return resultados


def generar_icg_normalizado(semilla: int, cantidad: int,
                             p: int = 1009,
                             a: int = 11,
                             c: int = 12):
    """
    Igual quelos valores reales, pero devuelve los valores 
    en el rango [0, 1) dividiendo entre p
    """
    enteros = generar_icg(semilla, cantidad, p, a, c)
    return [val / p for val in enteros]
 
semilla = int(input("Ingresa la semilla: "))
cantidad = int(input("Cantidad de numeros a generar: "))
 
numeros = generar_icg(semilla, cantidad)
print("\nNumeros pseudoaleatorios (enteros):")
print(numeros)
 
numeros_norm = generar_icg_normalizado(semilla, cantidad)
print("\nNumeros pseudoaleatorios (normalizados en [0,1)):")
print([round(v, 6) for v in numeros_norm])



maximo = round(max(numeros_norm), 6) 
minimo = round(min(numeros_norm),6)
promedio = round(sum(numeros_norm)/ len(numeros_norm), 6)

print(f"\n El numero maximo de esta lista es la siguiente: {maximo} ")


print(f"\n El numero minimo de esta lista es el siguiente: {minimo}" )


print(f"\n El promedio de los numeros es el siguiente: {promedio}")


