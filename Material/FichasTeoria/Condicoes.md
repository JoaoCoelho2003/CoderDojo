# Condições em Python

## Introdução

As condições são uma parte fundamental de qualquer linguagem de programação. Elas permitem que o programa tome decisões com base em certos critérios. Em Python, utilizamos as declarações `if`, `elif` e `else` para criar condições.

## Estrutura Básica

A estrutura básica de uma condição em Python é a seguinte:

```python
if condição:
    # código a ser executado se a condição for verdadeira
elif outra_condição:
    # código a ser executado se a outra condição for verdadeira
else:
    # código a ser executado se nenhuma das condições anteriores for verdadeira
```

## Exemplos

### Exemplo 1: Verificação de Número Positivo

```python
numero = 10

if numero > 0:
    print("O número é positivo.")
elif numero == 0:
    print("O número é zero.")
else:
    print("O número é negativo.")
```

### Exemplo 2: Verificação de Paridade

```python
numero = 4

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
```

## Operadores de Comparação

Os operadores de comparação são usados para comparar valores. Aqui estão alguns dos mais comuns:

- `==`: igual a
- `!=`: diferente de
- `>`: maior que
- `<`: menor que
- `>=`: maior ou igual a
- `<=`: menor ou igual a

## Operadores Lógicos

Os operadores lógicos são usados para combinar múltiplas condições:

- `and`: retorna `True` se ambas as condições forem verdadeiras
- `or`: retorna `True` se pelo menos uma das condições for verdadeira
- `not`: inverte o valor lógico

### Exemplo 3: Uso de Operadores Lógicos

```python
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir.")
else:
    print("Não pode dirigir.")
```

## Exercícios

### Exercício 1: Verificação de Maioridade

Escreva um programa que verifique se uma pessoa é maior de idade (18 anos ou mais).

### Exercício 2: Verificação de Nota

Escreva um programa que receba uma nota de 0 a 100 e imprima se o aluno foi aprovado (nota >= 60), está em recuperação (nota entre 40 e 59) ou foi reprovado (nota < 40).

### Exercício 3: Verificação de Triângulo

Escreva um programa que receba três lados de um triângulo e verifique se eles formam um triângulo válido. Um triângulo é válido se a soma de dois lados for sempre maior que o terceiro lado.

## Soluções

### Solução do Exercício 1

```python
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")
```

### Solução do Exercício 2

```python
nota = int(input("Digite a nota: "))

if nota >= 60:
    print("Aprovado.")
elif 40 <= nota < 60:
    print("Recuperação.")
else:
    print("Reprovado.")
```

### Solução do Exercício 3

```python
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Os lados formam um triângulo válido.")
else:
    print("Os lados não formam um triângulo válido.")
```
## Condições Aninhadas

As condições aninhadas são condições dentro de outras condições. Elas são úteis quando precisamos verificar múltiplas condições de forma hierárquica.

### Exemplo 4: Verificação de Intervalo

```python
numero = 15

if numero > 0:
    if numero < 10:
        print("O número está entre 1 e 9.")
    else:
        print("O número é 10 ou maior.")
else:
    print("O número é zero ou negativo.")
```

### Exemplo 5: Classificação de Idade

```python
idade = 25

if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")
```

## Exercícios Adicionais

### Exercício 4: Verificação de Ano Bissexto

Escreva um programa que verifique se um ano é bissexto. Um ano é bissexto se for divisível por 4, mas não por 100, exceto se for divisível por 400.

### Exercício 5: Classificação de IMC

Escreva um programa que calcule o Índice de Massa Corporal (IMC) e classifique o resultado em "Abaixo do peso", "Peso normal", "Sobrepeso" ou "Obesidade".

## Soluções Adicionais

### Solução do Exercício 4

```python
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Ano bissexto.")
else:
    print("Ano não bissexto.")
```

### Solução do Exercício 5

```python
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso.")
elif imc < 24.9:
    print("Peso normal.")
elif imc < 29.9:
    print("Sobrepeso.")
else:
    print("Obesidade.")
```