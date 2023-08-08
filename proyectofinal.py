import random                 # Libreria para genera los numeros alazar
import datetime               # Libreria que nos va dar la fecha y hora 

# Para generar los números ganadores para Quiniela y Quini 6
def generar_numeros_ganadores(tipo_apuesta, num_cifras=None):
    if tipo_apuesta == "1":
        # Para la Quiniela, se genera un número aleatorio con la cantidad de cifras apostada
        return random.randint(0, 10 ** num_cifras - 1)  #Nos va dar la misma cantidad que el numero apostado
    elif tipo_apuesta == "2":
        # Para Quini 6, se generan 6 números aleatorios entre 0 y 45
        return random.sample(range(0, 46), 6)  #Va a darnos 6 numeros aleatorios que serian los ganadores 

# Esto es la función para la opción de Quiniela
def quiniela():
    print("\n--- Quiniela Aposta y Gana ---")  #Nombre de quiniela
    nombre_quiniela = "Quiniela"
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H")   #Nos va indicar el año , mes ,dia y hora 
    num_comprobante = input("Ingresa el número de comprobante: ")
    dni_apostador = input("Ingresa el DNI del apostador: ")

    while True:
        try:
            num_cifras = int(input("Ingresa la cantidad de cifras (2, 3 o 4): "))
            if num_cifras not in [2, 3, 4]:
                raise ValueError
            break
        except ValueError:
            print("Ingresa un número (2, 3 o 4).")

    cifra_apostada = input(f"Ingresa el número {num_cifras} a apostar: ")

    while True:
        try:
            valor_apuesta = float(input("Ingresa el valor: "))
            if valor_apuesta <= 0:
                raise ValueError
            break
        except ValueError:
            print("Ingresa un valor válido.")

    # Crea el número ganador de la Quiniela aleatoriamente
    quiniela_ganadora = generar_numeros_ganadores("1", num_cifras)

    # Imprime el ticket comprobante de la quiniela y nos da datos de la jugada
    print("\n+" + "-" * 30 + "+")
    print(f"| Nombre del local: {nombre_quiniela} Aposta y Gana |")
    print("+" + "-" * 30 + "+")
    print(f"| Fecha y hora de la apuesta: {fecha_hora} |")    #El dia y hora que se jugo 
    print(f"| Número de comprobante: {num_comprobante} |")    #Numero del comprobante
    print(f"| DNI del apostador: {dni_apostador} |")
    print(f"| Cifra apostada: {cifra_apostada} |")  
    print(f"| Valor de la apuesta: ${valor_apuesta:.2f} |")   #Cantidad apostado 
    print("+" + "-" * 30 + "+")

    return valor_apuesta, quiniela_ganadora, num_cifras #Nos devuelve alguno de estas funciones

# La función para la opción de Quini 6 Tradicional
def quini_6_tradicional():
    print("\n--- Quiniela Aposta y Gana ---")
    nombre_quiniela = "Quini 6 Tradicional"
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H")
    num_comprobante = input("Ingresa el número de comprobante: ")
    dni_apostador = input("Ingresa el DNI del apostador: ")

    valor_apuesta = 400.0

    numeros_apostados = []
    modo_auto = input("¿Generar números al azar? (s/n): ")

    if modo_auto.lower() == "s":
        # Crea los números aleatorios para Quini 6 si el usuario quiere.
        numeros_apostados = random.sample(range(0, 46), 6)
    else:
        # Para ingresar manualmente los números del Quini 6
        print("Ingresa los seis números de 00 a 45 :")
        for i in range(6):
            numero = int(input(f"Número {i + 1}: "))
            numeros_apostados.append(numero)

    # Crea los números ganadores aleatoriamente del Quini 6
    quini6_ganadora = generar_numeros_ganadores("2")

    # Imprime  el ticket del comprobante 
    print("\n+" + "-" * 30 + "+")
    print(f"| Nombre del local: {nombre_quiniela} Aposta y Gana |")
    print("+" + "-" * 30 + "+")
    print(f"| Fecha y hora de la apuesta: {fecha_hora} |")
    print(f"| Número de comprobante: {num_comprobante} |")
    print(f"| DNI del apostador: {dni_apostador} |")
    print(f"| Cifras apostadas: {', '.join(str(num) for num in numeros_apostados)} |")
    print(f"| Valor de la apuesta: ${valor_apuesta:.2f} |")
    print("+" + "-" * 30 + "+")

    return valor_apuesta, numeros_apostados, quini6_ganadora

# Esto es la funcion para el arqueo de caja
def arqueo_de_caja(recaudacion_diaria):
    print("\n--- Quiniela Aposta y Gana ---")
    print("\n+" + "-" * 30 + "+")
    print("|        Arqueo de Caja        |")
    print("+" + "-" * 30 + "+")
    retencion = recaudacion_diaria * 0.47
    ganancia_neta = recaudacion_diaria - retencion

    print(f"| Recaudación diaria : ${recaudacion_diaria:.2f} |")
    print(f"| Retención (47%): ${retencion:.2f} |")
    print(f"| Ganancia para el quinielero: ${ganancia_neta:.2f} |")
    print("+" + "-" * 30 + "+")

# Comprobar si el cliente gano en Quiniela o en Quini 6.
def comprobar_apuesta(numeros_ganadores, tipo_apuesta, num_cifras=None):
    print("\n--- Quiniela Aposta y Gana ---")
    print("\n+" + "-" * 30 + "+")
    print("|     Comprobar Apuesta     |")
    print("+" + "-" * 30 + "+")

    num_comprobante = input("Ingresa el número de comprobante: ")

    if tipo_apuesta == "1":
        numeros_apostados = int(input(f"Ingresa el número de {num_cifras}a apostar: "))
    elif tipo_apuesta == "2":
        numeros_apostados = [int(input(f"Número {i + 1}: ")) for i in range(6)]

    print("\nNúmeros apostados:")
    if tipo_apuesta == "1":
        print(f"{numeros_apostados:0{num_cifras}d}")
    elif tipo_apuesta == "2":
        print(f"{', '.join(str(num) for num in numeros_apostados)}")

    print("\nNúmeros ganadores:")
    if tipo_apuesta == "1":
        print(f"{numeros_ganadores:0{num_cifras}d}")
    elif tipo_apuesta == "2":
        print(f"{', '.join(str(num) for num in numeros_ganadores)}")

    comprobar_quiniela = numeros_apostados == numeros_ganadores if tipo_apuesta == "1" else set(numeros_apostados) == set(numeros_ganadores)
    if comprobar_quiniela:
        print("\n¡Felicitaciones! ¡Ganaste!")
    else:
        print("\n No ganaste.")

# Función principal del programa
def main():
    recaudacion_diaria = 0

    while True:
        print("\n+" + "-" * 30 + "+")
        print("|   ¡Quiniela Aposta y Gana!   |")
        print("+" + "-" * 30 + "+")
        print("|          Opciones            |")
        print("+" + "-" * 30 + "+")
        print("| 1. Quiniela                  |")
        print("| 2. Quini 6 Tradicional       |")
        print("| 3. Arqueo de Caja            |")
        print("| 4. Comprobar Apuesta         |")
        print("| 5. Salir                     |")
        print("+" + "-" * 30 + "+")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            valor_apuesta, quiniela_ganadora, num_cifras = quiniela()
            recaudacion_diaria += valor_apuesta
        elif opcion == "2":
            valor_apuesta, numeros_apostados, quini6_ganadora = quini_6_tradicional()
            recaudacion_diaria += valor_apuesta
        elif opcion == "3":
            arqueo_de_caja(recaudacion_diaria)
        elif opcion == "4":
            print("\nSelecciona una opcion:")
            print("1: Quiniela")
            print("2: Quini 6")
            tipo_apuesta = input("Ingresa alguna opcion: ")

            if tipo_apuesta == "1":
                numeros_ganadores = generar_numeros_ganadores(tipo_apuesta, num_cifras)
                comprobar_apuesta(numeros_ganadores, tipo_apuesta, num_cifras)
            elif tipo_apuesta == "2":
                numeros_ganadores = generar_numeros_ganadores(tipo_apuesta)
                comprobar_apuesta(numeros_ganadores, tipo_apuesta)
            else:
                print("Opción Invalida.")
        elif opcion == "5":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción Invalida.")

if __name__ == "__main__":
    main()


