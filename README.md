# rest-api-com-Flask

API construída com Flask. È baseado em um banco de dados SQLITE.

## Configurações prévias

Para executar esse projeto, é necessário que seu sistema contenha as seguintes instalações:

### 1. Python

De preferência a versão mais recente.

### 2. Gerenciador de Pacotes do Python (Pip)

De preferência a versão mais recente também.

## Começando

### Clone o projeto

```shell
git clone https://github.com/gabrielmelhor2/rest-api-com-Flask.git
cd rest-api-com-Flask
```

### Instale as dependências

```python
pip install -r requirements.txt
```

### Acesse a documentação

A documentação poderá ser acessada através do endereço: `http://localhost:5000`

## Endpoints

> Os endpoints e seus receptivos acessos estão suscetíveis a mudança a medida que o projeto avança.

### Users

| Método |             Rota             |           Funcionalidade            | Acesso  |
| :----: | :--------------------------: | :---------------------------------: | :-----: |
|  GET   |     /books/api/v1/lista/     |       Obtém todos os livros.        | Público |
|  GET   |    /books/api/v1/lista/1     |        Obtém livros de id 1         | Público |
|  POST  |   /books/api/v1/lista/add/   |       Adiciona um novo livro.       | Público |
|  PUT   |  /books/api/v1/lista/put/1   | Atualiza os dados do livro de id 1. | Público |
| DELETE | /books/api/v1/lista/delete/1 |       Deleta o livro de id 1.       | Público |
