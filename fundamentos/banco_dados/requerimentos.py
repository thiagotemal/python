
try:
    from mysql import connector
except ModuleNotFoundError:
    print("MOdulo não encontrado")
else:
    print("modulo encontrado")