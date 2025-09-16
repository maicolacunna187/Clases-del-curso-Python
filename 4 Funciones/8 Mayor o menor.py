import random

def mostrar_reglas():
    print("""
    🃏 Juego: Mayor o Menor

    🎲 Aparece una carta entre 1 y 13
    ⬆️ Elige 'Mayor' si crees que la siguiente será más alta
    ⬇️ Elige 'Menor' si crees que la siguiente será más baja
    📖 Se revela la nueva carta
    ✅ Si acertaste, ganas la ronda
    ❌ Si fallas, pierdes la ronda
    ⚖️ Si son iguales → se repite la ronda (no cuenta)
    🔄 Juega varias rondas y suma tus aciertos!

""")

def choose_options():
    carta_inicial = random.randint(1,13)
    carta_nueva = random.randint(1,13)

    print(f"La carta seleccionada por la computadora es: {carta_inicial}.")

    user_respuesta = input("La siguiente carta será: 'Mayor' o 'Menor' que la actual: ").lower()
    while user_respuesta not in ("mayor", "menor"):
        user_respuesta = input("Debes escribir 'Mayor' o 'Menor':  ").lower()

    return user_respuesta, carta_inicial, carta_nueva

def check_rules(carta_inicial, carta_nueva, user_respuesta):

    if user_respuesta == "mayor":
        if carta_inicial < carta_nueva:
            print(f"✅ Correcto. La carta es MAYOR: {carta_nueva}")
            return "ganaste"
        elif carta_inicial == carta_nueva:
            print(f"⚖️ Las cartas son iguales: {carta_inicial} == {carta_nueva}")
            return "empate"
        else:
            print(f"❌ Incorrecto. La carta es MENOR: {carta_nueva}")
            return "perdiste"
    elif user_respuesta == "menor":
        if carta_inicial > carta_nueva:
            print(f"✅ Correcto. La carta es MENOR: {carta_nueva}")
            return "ganaste"
        elif carta_inicial == carta_nueva:
            print(f"⚖️ Las cartas son iguales: {carta_inicial} == {carta_nueva}")
            return "empate"
        else:
            print(f"❌ Incorrecto. La carta es MAYOR: {carta_nueva}")
            return "perdiste"

def verify_winner(user_hits, maximum_attempts):
    print("\n📊 GAME OVER")
    print("RESULTADO FINAL:")
    print(f"Has acertado {user_hits} de {maximum_attempts} rondas jugadas.")

    if user_hits == maximum_attempts:
        print("🏆 ¡Perfecto! No fallaste ninguna ronda.")
    elif user_hits >= maximum_attempts // 2:
        print("🎉 ¡Muy bien! Ganaste más de la mitad de las rondas.")
    else:
        print("😢 Perdiste más rondas de las que ganaste. ¡Sigue practicando!")

def run_game():

    maximum_attempts = 5
    user_count = 0
    user_hits = 0

    mostrar_reglas()

    while user_count < maximum_attempts:
        user_respuesta, carta_inicial, carta_nueva = choose_options()
        resultado_final = check_rules(carta_inicial, carta_nueva, user_respuesta)

        if resultado_final == "ganaste":
            user_hits += 1
            user_count += 1
        elif resultado_final == "perdiste":
            user_count += 1
        elif resultado_final == "empate":
            print("🔄 Ronda repetida, no cuenta en el marcador.")

    verify_winner(user_hits, maximum_attempts)

if __name__ == "__main__":
    while True:
        run_game()
        jugar_otra = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_otra != "s":
            print("👋 Gracias por jugar. ¡Hasta pronto!")
            break
