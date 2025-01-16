#!/usr/bin/python3
with open('pessoa.csv') as arquivo:
    for registro in arquivo:
        print('registro {} e {}'.format(*registro.strip().split(',')))

