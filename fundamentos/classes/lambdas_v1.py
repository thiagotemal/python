compras = [
    {"qtde": 10, "preco": 10},
    {"qtde": 2, "preco": 5},
    {"qtde": 2, "preco": 1}
]

total = tuple(map(lambda x: x['qtde'] * x["preco"], compras)

)


print("total", total)
print("soma", sum(total))
