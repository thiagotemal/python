# Operações com RabbitMQ em Python

Este projeto demonstra como realizar operações de envio e consumo de mensagens utilizando o RabbitMQ como broker de mensagens. O projeto utiliza a linguagem Python e a biblioteca `pika` para se comunicar com o RabbitMQ.

## Objetivo

O objetivo principal deste projeto é demonstrar como utilizar os tipos de exchanges comuns do RabbitMQ, incluindo:

* Fanout
* Direct
* Topic

Além disso, o projeto também demonstra como utilizar routing e headers para direcionar as mensagens para os consumidores corretos.

## Requisitos

Para executar este projeto, você precisará ter instalado:

* Python 3.x
* pip (gerenciador de pacotes do Python)
* Dependências listadas no arquivo `requirements.txt`

Além disso, você precisará ter o Docker instalado para subir o RabbitMQ. Você pode usar o comando abaixo para subir o RabbitMQ:
```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4.0-management

## Instalação
Para instalar as dependências, execute o comando abaixo:

pip install -r requirements.txt

##  Execução
Para executar o projeto, você pode usar o comando abaixo:

Para produzir
python producer_worker.py

python consumer_worker_auto_ack.py

Para consumir mensagem

##  Exemplos
O projeto inclui exemplos de como utilizar os diferentes tipos de exchanges e routing. Você pode encontrar os exemplos no arquivo main.py.

##  Documentação
Para mais informações sobre o RabbitMQ e a biblioteca pika, você pode consultar a documentação oficial:

RabbitMQ: https://www.rabbitmq.com/
Pika: https://pika.readthedocs.io/en/stable/
Contribuição
Se você deseja contribuir com o projeto, por favor, siga os seguintes passos:

Faça um fork do repositório do projeto.
Crie uma branch para sua contribuição: git checkout -b [nome da branch]
Faça suas alterações e commit: git commit -m [mensagem de commit]
Envie um pull request para o repositório original.