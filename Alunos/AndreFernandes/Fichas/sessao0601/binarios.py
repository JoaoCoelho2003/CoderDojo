def binarios(str):
    invertida = str [::-1]
    pos = 0 
    valor = 0
    for i in invertida:
        if i == "1":
            valor += pow(2,pos)
        pos +=1

    return valor

def main():
    valor = binarios("0001")
    print(valor)

if __name__ == "__main__":
    main()
