



def pares():
    lista = [1,2,3,4,5]
    pares = []
    for i in lista:
        if i % 2  != 0:
            pares.append(i)
    print(pares)

def vogal(str):
    vogais = "aeiouAEIOU"
    semvogais = ""
    for i in str:
        if i not in vogais:
            semvogais += i
    print(semvogais)



    



def main():
    pares()
    vogal("abcedario")


if __name__ == "__main__":
    main()

