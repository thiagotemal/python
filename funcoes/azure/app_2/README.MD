# Azure Functions - Funcion App

## Descrição

Este é um aplicativo de Azure Functions que contém várias funções para processamento de dados.

## Tecnologias Usadas

* Azure Functions
* Linguagem de programação: Python
* Framework: Azure Functions SDK

## Funções

* **Echo**: Função que responde a requisições HTTP com uma mensagem personalizada.
* **Recorrency**: Função que é executada periodicamente para realizar tarefas de manutenção.
* **ReadContainerFunction**: Função que lê um arquivo de um contêiner de armazenamento e processa seus dados.

## Instruções de Uso

1. Clone o repositório e navegue até a pasta do projeto.
2. Instale as dependências necessárias executando `pip install -r requirements.txt`.
3. Execute a função desejada usando o comando `func host start` e acesse a URL correspondente.

## Exemplos de Uso

* **Echo**: `http://localhost:7071/api/Echo?name=SeuNome`
* **Recorrency**: Não há URL correspondente, pois é uma função que é executada periodicamente.
* **ReadContainerFunction**: Não há URL correspondente, pois é uma função que lê um arquivo de um contêiner de armazenamento.

## Requisitos

* Azure Functions Core Tools
* Python 3.6 ou superior
* Azure Storage Emulator (opcional)

## Contribuição

Se você deseja contribuir com o projeto, por favor, [instruções de contribuição].

