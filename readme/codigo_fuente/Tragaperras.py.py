'''Juego Tragaperras para casino'''
'''Autor: Tyler Zamora'''
'''Grupo #3'''
import random

def mostrar_carretes(carretes):
    for i in range(3):
        print(" | ".join(carretes[i]))
        print("-----------------")

def generar_combinacion():
    simbolos = ["7", "🍒", "🔔", "💎", "🍀", "🎰"]
    return [random.choice(simbolos) for _ in range(3)]

def calcular_premio(comb):
    premios = {
        "🍒🍒🍒": 50,
        "💎💎💎": 100,
        "🔔🔔🔔": 200,
        "🎰🎰🎰": 1000,
    }

    combinacion = "".join(comb)
    if combinacion in premios:
        return premios[combinacion]
    else:
        return 0

def tragaperras():
    monedas = 100
    print("Bienvenido a la tragaperras. ¡Buena suerte!")
    
    while monedas > 0:
        print(f"Tienes {monedas} monedas.")
        apuesta = int(input("Ingresa tu apuesta (0 para salir): "))

        if apuesta == 0:
            break

        if apuesta > monedas:
            print("No tienes suficientes monedas para esa apuesta. Prueba con una cantidad menor.")
            continue

        monedas -= apuesta

        carretes = [generar_combinacion() for _ in range(3)]
        mostrar_carretes(carretes)

        premio = calcular_premio([carretes[i][1] for i in range(3)])  # Comparamos el símbolo del medio en cada carrete

        if premio > 0:
            monedas += premio
            print(f"¡Felicidades! Has ganado {premio} monedas.")
        else:
            print("No ha sido tu día. Sigue intentándolo.")

    print("Gracias por jugar. Vuelve pronto.")

tragaperras()
