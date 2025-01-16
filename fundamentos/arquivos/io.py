#!/usr/bin/python3

arquivo = open('pessoa.csv')
pessoas = arquivo.read()
arquivo.close()

for registro in pessoas.splitlines():
    print('registro {} e {}'.format(*registro.split(',')))
    