# Ciclos em Python

## Introdução
Os ciclos são estruturas de controlo de fluxo que permitem a repetição de um bloco de código várias vezes. Em Python, existem dois tipos principais de ciclos: `for` e `while`.

## Ciclo `for`
O ciclo `for` é usado para iterar sobre uma sequência (como uma lista, tupla, dicionário, conjunto ou string).

### Sintaxe
```python
for elemento in sequencia:
    # bloco de código a ser repetido
```

### Exemplo
```python
frutas = ["maçã", "banana", cereja"]
for fruta in frutas:
    print(fruta)
```

## Ciclo `while`
O ciclo `while` repete um bloco de código enquanto uma condição especificada for verdadeira.

### Sintaxe
```python
while condição:
    # bloco de código a ser repetido
```

### Exemplo
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

## Uso de `break` e `continue`
Os ciclos `for` e `while` podem ser controlados usando as instruções `break` e `continue`.

### `break`
A instrução `break` termina o ciclo imediatamente.

### Exemplo
```python
for numero in range(10):
    if numero == 5:
        break
    print(numero)
```

### `continue`
A instrução `continue` salta a iteração atual e continua com a próxima.

### Exemplo
```python
for numero in range(10):
    if numero % 2 == 0:
        continue
    print(numero)
```

## Conclusão
Os ciclos são ferramentas poderosas em Python que permitem a repetição de blocos de código de forma eficiente. Compreender como e quando usar `for` e `while` é essencial para escrever código Python eficaz.

## Exercícios

### Exercício 1: Ciclo `for` simples
Escreva um programa que imprima todos os números de 1 a 10 usando um ciclo `for`.

### Exercício 2: Ciclo `while` simples
Escreva um programa que imprima todos os números de 1 a 10 usando um ciclo `while`.

### Exercício 3: Soma de números
Escreva um programa que some todos os números de 1 a 100 usando um ciclo `for`.

### Exercício 4: Fatorial
Escreva um programa que calcule o fatorial de um número dado usando um ciclo `while`.

### Exercício 5: Números pares
Escreva um programa que imprima todos os números pares de 1 a 20 usando um ciclo `for` e a instrução `continue`.

## Soluções

### Solução do Exercício 1
```python
for numero in range(1, 11):
    print(numero)
```

### Solução do Exercício 2
```python
contador = 1
while contador <= 10:
    print(contador)
    contador += 1
```

### Solução do Exercício 3
```python
soma = 0
for numero in range(1, 101):
    soma += numero
print(soma)
```

### Solução do Exercício 4
```python
numero = 5  # exemplo de número
fatorial = 1
while numero > 1:
    fatorial *= numero
    numero -= 1
print(fatorial)
```

### Solução do Exercício 5
```python
for numero in range(1, 21):
    if numero % 2 != 0:
        continue
    print(numero)
```