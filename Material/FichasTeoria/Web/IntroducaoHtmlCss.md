# **Guia Introdutório a HTML e CSS**

Este guia tem como objetivo ensinar os conceitos básicos de HTML e CSS, essenciais para criar páginas web estruturadas e estilizadas. O conteúdo abrange a introdução, explicação das principais tags HTML, exemplos práticos e exercícios.


## **1. Introdução ao HTML**

O HTML (HyperText Markup Language) é a linguagem de marcação usada para estruturar o conteúdo da web. Ela utiliza **tags** que identificam os diferentes tipos de elementos numa página, como texto, imagens, links e vídeos.

### **Exemplo Básico de Estrutura HTML**
```html
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minha Primeira Página</title>
</head>
<body>
    <h1>Bem-vindo ao HTML</h1>
    <p>Esta é a minha primeira página HTML.</p>
</body>
</html>
```
## 2. Estrutura Básica de um Documento HTML

**Tags Principais:**

- `<html>:` Envolve todo o conteúdo da página;
- `<head>:` Contém informações como o título da página e links para recursos externos;
- `<body>:` Contém o conteúdo visível da página;

### Exercício:

+ Crie um ficheiro `index.html`;
+ Reproduza a estrutura básica de um documento HTML.
+ Altere o título no `<head>` e adicione um parágrafo no `<body>`.

## 3. Tipos de Tags HTML

### 3.1 Tags de Conteúdo de Texto

- `<h1> a <h6>:` Criam títulos (do maior ao menor);
- `<p>:` Define parágrafos;
- `<span>:` Destaca partes específicas do texto;
- `<strong>:` Texto em negrito;
- `<em>:` Texto em itálico;
- `<br>:` Insere uma quebra de linha.

#### Exemplo

```html
<h1>Título Principal</h1>
<p>Este é um parágrafo com <strong>texto em negrito</strong> e <em>texto em itálico</em>.</p>
```

### Exercício

- Crie títulos `<h1>` a `<h6>` com textos diferentes;
- Adicione um parágrafo com palavras destacadas em negrito e itálico.

### 3.2 Tags para Mídia

- `<img>:` Insere imagens;
- `<video>:` Adiciona vídeos;
- `<audio>:` Reproduz áudio;
- `<iframe>:` Insere conteúdos externos.

#### Exemplo

```html
<img src="imagens/imagem.jpg" alt="Descrição da imagem">
<video controls>
    <source src="videos/example.mp4" type="video/mp4">
</video>
```

### Exercício

- Insira uma imagem com a tag `<img>`;
- Adicione um vídeo utilizando a tag `<video>`.

### 3.3 Tags de Links e Listas

- `<a>:` Cria links;
- `<ul>:` Lista não ordenada;
- `<ol>:` Lista ordenada;
- `<li>:` Itens da lista.

#### Exemplo

```html
<a href="https://coderdojobraga.org/">Visite o site</a>
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>
```

### Exercício

- Crie um link para o Google;
- Adicione uma lista ordenada e uma lista não ordenada.

### 3.4 Tags de Organização e Layout

- `<div>:` Agrupa elementos;
- `<section>:` Define seções;
- `<header> e <footer>:` Cabeçalho e rodapé.

### Exemplo

```html
<header>
    <h1>Meu Site</h1>
</header>
<section>
    <p>Secção de conteúdo.</p>
</section>
<footer>
    <p>© 2024 Meu Site</p>
</footer>
```

### Exercício

- Crie um cabeçalho e um rodapé;
- Adicione uma seção com parágrafos.

## 4. Introdução ao CSS

O CSS (Cascading Style Sheets) permite estilizar os elementos HTML, controlando cores, fontes, tamanhos, espaçamentos e muito mais. O CSS pode ser aplicado de duas maneiras: inline ou em um ficheiro externo.

### Exemplo de CSS Inline

```html
<!DOCTYPE html>
<html lang="pt">
<head>
    <title>Exemplo CSS Inline</title>
</head>
<body>
    <h1 style="color: #0066cc;">Bem-vindo ao CSS Inline</h1>
    <p style="font-family: Arial, sans-serif; background-color: #f0f0f0; color: #333;">
        Com o CSS inline, podemos estilizar elementos diretamente no HTML.
    </p>
</body>
</html>
```

### Exemplo de CSS em Ficheiro Externo

```html
<!DOCTYPE html>
<html lang="pt">
<head>
    <link rel="stylesheet" href="styles.css">
    <title>Exemplo CSS Externo</title>
</head>
<body>
    <h1>Bem-vindo ao CSS Externo</h1>
    <p>Com o CSS externo, podemos estilizar nossas páginas de forma mais organizada.</p>
</body>
</html>
```

**styles.css**

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    color: #333;
}
h1 {
    color: #0066cc;
}
```


