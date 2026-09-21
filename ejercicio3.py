

def icg_stream(semilla, p=2147483647, a=1103515245, c=12345):
   
    def inverso_modular(x, modulo):
        if x == 0:
            return 0
        return pow(x, modulo - 2, modulo)

    x = semilla
    while True:
        x = (a * inverso_modular(x, p) + c) % p
        yield x / p


def simular_propagacion(poblacion, lugares, prob_contagio, semilla=1, dias_maximo=100000):
  
    generador = icg_stream(semilla)

    infectado = [False] * poblacion
    infectado[0] = True  # paciente cero

    objetivo = poblacion * 0.8
    dias = 0

    while sum(infectado) < objetivo:
        dias += 1

       
        asignacion = []
        for _ in range(poblacion):
            valor = next(generador)
            lugar = int(valor * lugares)
            if lugar == lugares: 
                lugar = lugares - 1
            asignacion.append(lugar)

      
        lugares_con_infectados = set()
        for persona in range(poblacion):
            if infectado[persona]:
                lugares_con_infectados.add(asignacion[persona])

        nuevos_infectados = []
        for persona in range(poblacion):
            if not infectado[persona] and asignacion[persona] in lugares_con_infectados:
                valor = next(generador)
                if valor < prob_contagio:
                    nuevos_infectados.append(persona)

        for persona in nuevos_infectados:
            infectado[persona] = True

        if dias >= dias_maximo:
            return None 

    return dias


poblacion = int(input("Numero de habitantes de la poblacion: "))
lugares = int(input("Numero de lugares de asistencia masiva: "))
prob_contagio = float(input("Probabilidad de contagio (0 a 1): "))

dias_resultado = simular_propagacion(poblacion, lugares, prob_contagio)

if dias_resultado is None:
    print("\nEl virus no logro infectar al 80% de la poblacion en un tiempo razonable.")
else:
    print(f"\nEl virus tardo {dias_resultado} dia(s) en infectar al 80% de la poblacion.")