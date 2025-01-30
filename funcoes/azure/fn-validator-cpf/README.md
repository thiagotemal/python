# Azure Function: Validação de CPF

Este projeto é uma Azure Function que realiza a validação de CPF (Cadastro de Pessoas Físicas) brasileiro.

## Funcionalidade

A função recebe uma requisição HTTP com um CPF como parâmetro e retorna uma resposta indicando se o CPF é válido ou não.

## Requisitos para Execução

* Azure Functions Core Tools (instalado via npm ou chocolatey)
* Python 3.6 ou superior
* Bibliotecas necessárias:
    + `azure-functions` (instalado via pip)
    + `json` (instalado via pip)
    + `logging` (instalado via pip)

## Ferramentas Utilizadas

* Azure Functions Core Tools
* Python 3.6
* Visual Studio Code (opcional)

## Arquivo `function_app.py`

Este arquivo contém a lógica da função Azure que realiza a validação de CPF.

```python
import logging
import json
from azure.functions import HttpResponse

def main(req: func.HttpRequest) -> HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        data = get_validated_data(req)
        cpf = data.get("cpf")
        if cpf and isinstance(cpf, str):
            if validate_cpf(cpf):
                return func.HttpResponse(
                    status_code=200, body=json.dumps({"valid": True})
                )
            else:
                return func.HttpResponse(
                    status_code=400, body=json.dumps({"valid": False})
                )
    except ValueError:
        return func.HttpResponse(
            status_code=400,
            body=json.dumps({"error": "Requisição inválida"})
        )

 # Instruções de Uso

1. Clone o repositório e navegue até a pasta do projeto.
2. Instale as dependências necessárias executando `pip install -r requirements.txt`.
3. Execute a função desejada usando o comando `func host start` e acesse a URL correspondente.

## Exemplos de Uso

1.  Instale as dependências necessárias via pip: pip install azure-functions json logging
2.  Execute a função Azure via Azure Functions Core Tools: func host start
3.  Envie uma requisição HTTP para a função Azure com um CPF como parâmetro: curl -X POST -H "Content-Type: application/json" -d '{"cpf": "12345678901"}' http://localhost:7071/api/validacpf

A resposta da função Azure será um JSON indicando se o CPF é válido ou não:
{
    "valid": true
}

ou
{
    "valid": false
}
## Requisitos

* Azure Functions Core Tools
* Python 3.6 ou superior
* Azure Storage Emulator (opcional)

## Contribuição

Se você deseja contribuir com o projeto, por favor, [instruções de contribuição].

       