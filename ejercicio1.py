"""
Generador Congruencial Inversivo (ICG - Inversive Congruential Generator)

Formula:
    x_(n+1) = (a * inv(x_n) + c) mod p

donde inv(x_n) es el inverso multiplicativo de x_n modulo p (p primo),
y por convencion inv(0) = 0.

Como p es primo, el inverso modular se calcula con el pequeño teorema
de Fermat: inv(x) = x^(p-2) mod p, usando pow(x, p-2, p) de Python
(muy eficiente, exponenciacion modular rapida).
"""


def generar_icg(semilla: int, cantidad: int,
                 p: int = 2147483647,   # primo grande (2^31 - 1, primo de Mersenne)
                 a: int = 1103515245,
                 c: int = 12345):
    """
    Genera una lista de numeros pseudoaleatorios usando un ICG.

    Parametros:
        semilla  (int): valor inicial x0, debe cumplir 0 <= semilla < p
        cantidad (int): cuantos numeros generar
        p (int): modulo, debe ser primo
        a (int): multiplicador
        c (int): incremento

    Retorna:
        list[int]: lista de 'cantidad' numeros pseudoaleatorios en [0, p-1]
    """
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
                             p: int = 2147483647,
                             a: int = 1103515245,
                             c: int = 12345):
    """
    Igual que generar_icg, pero devuelve los valores normalizados
    en el rango [0, 1) dividiendo entre p.
    """
    enteros = generar_icg(semilla, cantidad, p, a, c)
    return [val / p for val in enteros]


if __name__ == "__main__":
    semilla = int(input("Ingresa la semilla: "))
    cantidad = int(input("Cantidad de numeros a generar: "))

    numeros = generar_icg(semilla, cantidad)
    print("\nNumeros pseudoaleatorios (enteros):")
    print(numeros)

    numeros_norm = generar_icg_normalizado(semilla, cantidad)
    print("\nNumeros pseudoaleatorios (normalizados en [0,1)):")
    print([round(v, 6) for v in numeros_norm])