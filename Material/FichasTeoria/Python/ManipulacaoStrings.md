# Manipulação de Strings

## O que são Strings?

Strings são sequências de caracteres, como letras, números e símbolos. Em programação, usamos strings para representar texto. Por exemplo, `"Olá, Mundo!"` é uma string.

## Operações Básicas com Strings

### Concatenar Strings

Concatenar significa juntar duas ou mais strings. Podemos usar o operador `+` para fazer isso.

```python
nome = "João"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print(nome_completo)  # Output: João Silva
```

### Acessar Caracteres

Podemos acessar caracteres individuais de uma string usando índices. Lembre-se que os índices começam em 0.

```python
palavra = "CoderDojo"
primeira_letra = palavra[0]
print(primeira_letra)  # Output: C
```

### Fatiar Strings

Fatiar significa pegar uma parte da string. Podemos usar a notação `[inicio:fim]`.

```python
palavra = "CoderDojo"
primeiras_tres_letras = palavra[0:3]
print(primeiras_tres_letras)  # Output: Cod
```

### Comprimento da String

Podemos usar a função `len()` para obter o comprimento de uma string.

```python
palavra = "CoderDojo"
comprimento = len(palavra)
print(comprimento)  # Output: 9
```

### Métodos Úteis

- `upper()`: Converte todos os caracteres para maiúsculas.
- `lower()`: Converte todos os caracteres para minúsculas.
- `replace(antigo, novo)`: Substitui uma substring por outra.

```python
palavra = "CoderDojo"
print(palavra.upper())  # Output: CODERDOJO
print(palavra.lower())  # Output: coderdojo
print(palavra.replace("Dojo", "Camp"))  # Output: CoderCamp
```

## Exercícios

### Básicos

1. Cria uma string com o teu nome e imprime-a.

2. Junta duas strings e imprime o resultado.

3. Acede e imprime a terceira letra de uma string.

4. Converte uma string para maiúsculas e imprime-a.

### Intermediários

1. Pede ao utilizador para inserir uma frase e conta quantos caracteres ela tem.

2. Substitui todas as ocorrências de uma palavra numa string por outra palavra.

### Avançados

1. Cria uma função que inverta uma string.

2. Verifica se uma string é um palíndromo (lê-se da mesma forma de trás para frente).

## Soluções

### Básicos

1. 
```python
nome = "João"
print(nome)
```

2. 
```python
string1 = "Olá"
string2 = "Mundo"
resultado = string1 + " " + string2
print(resultado)  # Output: Olá Mundo
```

3. 
```python
palavra = "CoderDojo"
terceira_letra = palavra[2]
print(terceira_letra)  # Output: d
```

4. 
```python
palavra = "CoderDojo"
print(palavra.upper())  # Output: CODERDOJO
```

### Intermediários

1. 
```python
frase = input("Insere uma frase: ")
comprimento = len(frase)
print("A frase tem", comprimento, "caracteres.")
```

2. 
```python
frase = "Eu gosto de programar em Python"
nova_frase = frase.replace("Python", "JavaScript")
print(nova_frase)  # Output: Eu gosto de programar em JavaScript
```

### Avançados

1. 
```python
def inverter_string(s):
    return s[::-1]

print(inverter_string("CoderDojo"))  # Output: ojoDredoC
```

2. 
```python
def eh_palindromo(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(eh_palindromo("A base do teto desaba"))  # Output: True
```