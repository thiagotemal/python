#!/usr/bin/python3

from functools import reduce


lista = [
    {"nome": "JORTGE", "idade":50},

    {"nome":"pedtro", "idade": 10},
    {"nome": "ramiro", "idade":100},
    {"nome": "valentim", "idade": 200}
]

soidades = map(lambda x: x["idade"], lista)
print(f"idades {list(soidades)}")


soma = reduce(lambda idades, idade: idades + idade, soidades, 0)

print(soma)