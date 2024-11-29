## Estruturas Complexas

### Listas (List)

As listas são coleções ordenadas de elementos que podem ser de diferentes tipos. Elas são mutáveis, o que significa que podemos alterar seus elementos após a criação. As listas são úteis quando precisamos armazenar uma sequência de itens e acessar esses itens por meio de um índice.

Criar uma lista:

```python
frutas = ["maçã", "banana", "laranja"]
```

Adicionar um item à lista:

```python
frutas.append("uva")
```

Remover um item da lista:

```python
frutas.remove("banana")
```

Percorrer uma lista:

```python
for fruta in frutas:
    print(fruta)
```

Os índices em uma lista começam em 0. Por exemplo, `frutas[0]` retorna "maçã".

### Conjuntos (Set)

Os conjuntos são coleções não ordenadas de elementos únicos. Eles são úteis para armazenar itens quando a ordem não importa e não queremos duplicatas. Conjuntos suportam operações matemáticas como união, interseção e diferença.

Criar um conjunto:

```python
numeros = {1, 2, 3, 4}
```

Adicionar um item ao conjunto:

```python
numeros.add(5)
```

Remover um item do conjunto:

```python
numeros.remove(3)
```

Percorrer um conjunto:

```python
for numero in numeros:
    print(numero)
```

### Dicionários (Dict)

Os dicionários são coleções de pares chave-valor. Eles são úteis para armazenar dados que precisam ser associados a uma chave única. As chaves devem ser imutáveis, como strings ou números, e os valores podem ser de qualquer tipo.

Criar um dicionário:

```python
aluno = {"nome": "João", "idade": 10, "altura": 1.75}
```

Adicionar um par chave-valor ao dicionário:

```python
aluno["peso"] = 60.5
```

Remover um par chave-valor do dicionário:

```python
del aluno["altura"]
```

Percorrer um dicionário:

```python
for chave, valor in aluno.items():
    print(chave, valor)
```

## Exercícios sobre a matéria abordada

1. Cria uma lista chamada `animais` com os seguintes elementos: "cão", "gato", "pássaro".

2. Adiciona o elemento "peixe" à lista `animais`.

3. Remove o elemento "gato" da lista `animais`.

4. Cria um conjunto chamado `cores` com os seguintes elementos: "vermelho", "verde", "azul".

5. Adiciona o elemento "amarelo" ao conjunto `cores`.

6. Remove o elemento "verde" do conjunto `cores`.

7. Cria um dicionário chamado `carro` com os seguintes pares chave-valor: "marca": "Toyota", "modelo": "Corolla", "ano": 2020.

8. Adiciona o par chave-valor "cor": "preto" ao dicionário `carro`.

9. Remove o par chave-valor "ano" do dicionário `carro`.

### Exercícios adicionais

10. Ordena a lista `animais` em ordem alfabética.

11. Inverte a ordem da lista `animais`.

12. Verifica se o elemento "peixe" está presente na lista `animais`.

13. Cria um conjunto chamado `numeros_pares` com os números pares de 1 a 10.

14. Calcula a interseção entre os conjuntos `numeros` e `numeros_pares`.

15. Cria um dicionário chamado `livro` com os seguintes pares chave-valor: "título": "Python para Iniciantes", "autor": "Maria Silva", "páginas": 300.

16. Atualiza o valor da chave "páginas" para 350 no dicionário `livro`.

17. Verifica se a chave "autor" está presente no dicionário `livro`.

18. Itera sobre os elementos da lista `animais` e imprime cada um deles.

19. Itera sobre os pares chave-valor do dicionário `carro` e imprime cada um deles.

20. Cria uma lista chamada `numeros` com os números de 1 a 5 e calcula a soma de todos os elementos da lista.

## Soluções

```
1.
animais = ["cão", "gato", "pássaro"]

2.
animais.append("peixe")

3.
animais.remove("gato")

4.
cores = {"vermelho", "verde", "azul"}

5.
cores.add("amarelo")

6.
cores.remove("verde")

7.
carro = {"marca": "Toyota", "modelo": "Corolla", "ano": 2020}

8.
carro["cor"] = "preto"

9.
del carro["ano"]

10.
animais.sort()  

11.
animais.reverse()

    or

animais = animais[::-1]

12.
"peixe" in animais

13.
def numeros_pares():
    return {x for x in range(1, 11) if x % 2 == 0}

14.
def intersecao(conjunto1, conjunto2):
    return conjunto1 & conjunto2

15.
livro = {"título": "Python para Iniciantes", "autor": "Maria Silva", "páginas": 300}

16.
livro["páginas"] = 350

17.
"autor" in livro

18.
for animal in animais:
    print(animal)

19.
for chave, valor in carro.items():
    print(chave, valor)

20.
numeros = [1, 2, 3, 4, 5]
soma = sum(numeros)
```