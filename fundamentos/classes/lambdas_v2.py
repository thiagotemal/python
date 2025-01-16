lista = [
    {"nome": "JORTGE", "idade":50},

    {"nome":"pedtro", "idade": 10}
]

frases = (map(lambda x: f'{x["nome"]} tem {x["idade"]} anos', lista))
print(list(frases))