lista = [
    {"nome": "JORTGE", "idade":50},

    {"nome":"pedtro", "idade": 10},
    {"nome": "ramiro", "idade":100},
    {"nome": "valentim", "idade": 200}
]

frases = filter(lambda x: len(x["nome"]) >6, lista)
print(list(frases))