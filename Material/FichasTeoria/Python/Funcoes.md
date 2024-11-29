# Funções em Python

## O que são Funções?

As funções em Python são blocos de código reutilizáveis que realizam uma tarefa específica. Elas ajudam a tornar o código mais modular e fácil de entender. Uma função pode receber entradas, chamadas de argumentos, e pode opcionalmente retornar um valor.

## Para que servem?

As funções são usadas para:
- Reutilizar código.
- Dividir um problema grande em subproblemas menores.
- Melhorar a legibilidade e manutenção do código.
- Abstrair a complexidade, permitindo que o usuário da função não precise entender os detalhes internos de sua implementação.

## Como se fazem?

Para definir uma função em Python, usa-se a palavra-chave `def` seguida do nome da função e parênteses. O corpo da função é indentado.

### Exemplo:

```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("João")
```

Neste exemplo, a função `saudacao` recebe um parâmetro `nome` e imprime uma mensagem de saudação personalizada. Quando chamamos `saudacao("João")`, a saída será `Olá, João!`.

## Argumentos e Parâmetros

- **Parâmetros:** São variáveis listadas na definição da função.
- **Argumentos:** São os valores passados para a função quando ela é chamada.

### Tipos de Argumentos

1. **Argumentos Posicionais:** São passados para a função na ordem em que os parâmetros foram definidos.
2. **Argumentos Nomeados:** São passados na forma `nome=valor`, permitindo especificar quais parâmetros recebem quais valores.
3. **Argumentos Padrão:** São valores padrão atribuídos aos parâmetros, usados se nenhum argumento for fornecido.
4. **Argumentos Arbitrários:** Permitem passar um número variável de argumentos para uma função.

### Exemplo de Argumentos

#### Argumentos Posicionais

```python
def subtracao(a, b):
    return a - b

resultado = subtracao(10, 5)
print(resultado)  # Saída: 5
```

#### Argumentos Nomeados

```python
def subtracao(a, b):
    return a - b

resultado = subtracao(b=5, a=10)
print(resultado)  # Saída: 5
```

#### Argumentos Padrão

```python
def saudacao(nome="Mundo", saudacao="Olá"):
    print(f"{saudacao}, {nome}!")

saudacao()  # Saída: Olá, Mundo!
saudacao(nome="Ana")  # Saída: Olá, Ana!
saudacao(saudacao="Oi", nome="Carlos")  # Saída: Oi, Carlos!
```

#### Argumentos Arbitrários

```python
def soma(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

resultado = soma(1, 2, 3, 4)
print(resultado)  # Saída: 10
```

## Utilidades

- **Modularidade:** Permite dividir o código em partes menores e mais gerenciáveis.
- **Reutilização:** Evita a duplicação de código.
- **Abstração:** Esconde a complexidade dos detalhes de implementação.

## Exemplos de Funções

### Função sem parâmetros

```python
def ola_mundo():
    print("Olá, Mundo!")

ola_mundo()
```

Esta função `ola_mundo` não recebe parâmetros e simplesmente imprime "Olá, Mundo!" quando chamada.

### Função com parâmetros

```python
def soma(a, b):
    return a + b

resultado = soma(3, 4)
print(resultado)
```

A função `soma` recebe dois parâmetros `a` e `b`, e retorna a soma deles. No exemplo, `soma(3, 4)` retorna `7`, que é então impresso.

### Função com valor padrão

```python
def saudacao(nome="Mundo"):
    print(f"Olá, {nome}!")

saudacao()
saudacao("Ana")
```

Aqui, a função `saudacao` tem um parâmetro `nome` com valor padrão "Mundo". Se nenhum argumento for passado, ela usa o valor padrão. `saudacao()` imprime "Olá, Mundo!" e `saudacao("Ana")` imprime "Olá, Ana!".

### Função com múltiplos retornos

```python
def operacoes(a, b):
    soma = a + b
    diferenca = a - b
    return soma, diferenca

resultado_soma, resultado_diferenca = operacoes(5, 3)
print(f"Soma: {resultado_soma}, Diferença: {resultado_diferenca}")
```

A função `operacoes` retorna dois valores: a soma e a diferença dos parâmetros `a` e `b`. No exemplo, `operacoes(5, 3)` retorna `(8, 2)`, que são atribuídos a `resultado_soma` e `resultado_diferenca`, respectivamente.

## Exercícios

### Exercício 1: Função para calcular o quadrado de um número

Escreva uma função chamada `quadrado` que recebe um número como parâmetro e retorna o seu quadrado.

### Exercício 2: Função para verificar se um número é par

Escreva uma função chamada `eh_par` que recebe um número como parâmetro e retorna `True` se o número for par e `False` caso contrário.

### Exercício 3: Função para contar vogais

Escreva uma função chamada `conta_vogais` que recebe uma string e retorna o número de vogais na string.

### Exercício 4: Função para calcular o fatorial

Escreva uma função chamada `fatorial` que recebe um número inteiro não negativo e retorna o seu fatorial.

## Soluções

### Solução do Exercício 1

```python
def quadrado(numero):
    return numero ** 2
```

### Solução do Exercício 2

```python
def eh_par(numero):
    return numero % 2 == 0
```

### Solução do Exercício 3

```python
def conta_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in texto:
        if char in vogais:
            contador += 1
    return contador
```

### Solução do Exercício 4

```python
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
```

