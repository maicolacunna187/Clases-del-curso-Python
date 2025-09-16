import random

def mostrar_reglas(intentos):
    print("""
    🎮 Juego: Adivina el Número

    🤖 La computadora piensa un número secreto entre 1 y 10
    ❓ Tu misión: adivinarlo
    🔢 Cada vez que intentes:
    👉 La compu dirá si el número es más alto ⬆️ o más bajo ⬇️
    🏁 El juego termina cuando:
    ✅ Aciertas el número secreto
    ❌ Se acaban los intentos
    """)
    print(f"Tienes {intentos} intentos. ¡Mucha suerte!\n")


def choose_options():
    while True:
        try:
            user_option = int(input("Ingresa un número (1 - 10): "))
            if 1 <= user_option <= 10:
                return user_option
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número válido.")


def check_rules(user_option, computer_option):
    if user_option == computer_option:
        print("🎯 ¡Correcto, número adivinado!")
        return True
    elif user_option < computer_option:
        print("El número secreto es mayor.")
        return False    
    else:
        print("El número secreto es menor.")
        return False


def verify_winner(computer_opction,user_round, acertado):
    print("\nRESULTADO FINAL:")
    if acertado:
        print(f"✅ ¡Ganaste! Lo adivinaste en {user_round} intentos.")
    else:
        print(f"❌ Perdiste. El número secreto era {computer_opction}.")
        print("Buena suerte para la próxima.")


def run_game():
    max_intentos = 5
    mostrar_reglas(max_intentos)

    computer_option = random.randint(1, 10)
    user_round = 0
    acertado = False

    while user_round < max_intentos:
        print(f"\nIntento {user_round + 1} de {max_intentos}")
        user_option = choose_options()

        if check_rules(user_option, computer_option):
            acertado = True
            break
        user_round += 1

    verify_winner(computer_option, user_round + (1 if acertado else 0), acertado)
    

if __name__ == "__main__":
    while True:
        run_game()
        jugar_otra = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_otra != "s":
            print("Gracias por jugar. ¡Hasta pronto!")
            break
