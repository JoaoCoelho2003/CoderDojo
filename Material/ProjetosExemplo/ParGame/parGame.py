import random

def par_ou_impar():
    won = True
    while(won):
        print("Par ou Ímpar")
        print("Escolha entre par ou ímpar")
        print("1. Par")
        print("2. Ímpar")
        escolha = input("Digite a sua escolha: ")
        if escolha != "1" and escolha != "2":
            print("Escolha inválida")
            continue
        
        player_number = random.randint(0, 10)
        computer_number = random.randint(0, 10)

        print(f"Tu escolheste {player_number}")
        print(f"O computador escolheu {computer_number}")

        total = player_number + computer_number

        print(f"O total é {total}")

        if total % 2 == 0:
            if escolha == "1":
                print("Ganhaste")
            else:
                print("Perdeste")
                won = False

def main():
    par_ou_impar()

if __name__ == "__main__":
    main()