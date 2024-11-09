def corrida():
    print('Já corri mais 1 km')

def forRecursivo(function, iterations):
    if iterations > 0:
        function()
        forRecursivo(function, iterations - 1)

def main():
    forRecursivo(corrida, 5)

if __name__ == '__main__':
    main()