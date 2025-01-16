#!/usr/bin/python3
try:
    arquivo = open('pessoa.csv')


    for registro in arquivo:
        print('registro {} e {}'.format(*registro.strip().split(',')))
finally:
    print('FInally')
    arquivo.close()