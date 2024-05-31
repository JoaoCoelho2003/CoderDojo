# Rock Paper Scissors Game

import random

def game_logic():

    choices = ["Rock", "Paper", "Scissors"]

    won = True

    while(won):

        print("Escolha uma das seguintes opções")

        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")

        user_choice = int(input("Escolha: "))

        if user_choice == 1:
            user_choice = "Rock"

        elif user_choice == 2:
            user_choice = "Paper"

        elif user_choice == 3:
            user_choice = "Scissors"

        else:
            print("Opção inválida")
            continue

        computer_choice = random.choice(list(choices))

        print("Escolheste: ", user_choice)
        print("O computador escolheu: ", computer_choice)

        if user_choice == computer_choice:
            print("Empate")
        
        elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
            print("Ganhaste")
            won = False

        else:
            print("Perdeste")


def main():
    game_logic()

if __name__ == "__main__":
    main()


