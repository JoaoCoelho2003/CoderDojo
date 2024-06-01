import random
def menu():
    valida = True 
    while valida:
        print("par ou impar")
        print("1-par")
        print("2-impar")
        escolha=input ("escolha uma das seguintes opções: ")
        if escolha != "1" and escolha != "2":
            print("escolha inválida")
        else:
            valida = False
    return escolha
    
def game():
    escolha = menu()
    jogador= random.randint(0,10)
    print(jogador)
    adversario= random.randint(0,10)
    print(adversario)
    soma = jogador + adversario
    if soma % 2 == 0 and escolha == "1":
        print("you won")
    else:
        print("you lose") 

def main():
    game()

if __name__ == "__main__":
    main()