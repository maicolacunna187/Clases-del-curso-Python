
import random

def mostrar_reglas():
    print("""
    🎮 Juego: Par o Impar

    👤 Tú y 🤖 la computadora eligen un número del 1 al 5
    ➕ Se suman ambos números
    ⚖️ Si la suma es PAR y elegiste PAR → ganas 🎉
    ⚖️ Si la suma es IMPAR y elegiste IMPAR → ganas 🎉
    ❌ De lo contrario → gana la computadora 🤖
    """)
    
def choose_options():
    user_option = input("Quiere jugar con par o con impar: ").lower()
    while user_option not in ("par", "impar"):
        user_option = input("Debes escribir 'par' o 'impar': ").lower()
    while True:
        try:
            user_number = int(input("Ingrese un número (1 - 5): "))
            if 1 <= user_number <= 5:
                return user_option, user_number
            else:
                print("El número debe estar entre 1 y 5.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número válido.")
    

def check_rules(user_option, user_number ,computer_number):

    result = user_number + computer_number

    print(f"Tú elegiste: {user_option} con el número {user_number}")
    print(f"La computadora eligió: {computer_number}")
    print(f"La suma es: {result}")

    if user_option == "par":
        if result % 2 == 0:
            print("🎯 ¡Correcto, el resultado es Par!")
            return True
        else:
            print("Incorrecto, el resultado es Impar!")
            return False    
    elif user_option == "impar":
        if result % 2 != 0:
            print("🎯 ¡Correcto, el resultado es Impar!")
            return True
        else:
            print("Incorrecto, el resultado es Par!")
            return False

def verify_winner(computer_number, acertado):

    if acertado:
        print(f"✅ ¡Ganaste! Le ganaste al computador.")
    else:
        print(f"❌ Perdiste. El número del computer fue {computer_number}.")
        print("Buena suerte para la próxima.")

def run_game():
    mostrar_reglas()

    computer_number = random.randint(1,5)
    acertado = False

    user_option, user_number = choose_options()

    if check_rules(user_option, user_number, computer_number):
        acertado = True
    
    verify_winner(computer_number, acertado)


if __name__ == "__main__":
    while True:
        run_game()
        jugar_otra = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_otra != "s":
            print("Gracias por jugar. ¡Hasta pronto!")
            break  









