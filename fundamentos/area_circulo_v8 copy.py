#!/usr/bin/python3
from math import pi
import sys
import errno

def circulo(area):
    print('Area do Circulo ', pi * float(area) ** 2)
    

if __name__=='__main__':
    if len(sys.argv) <2:
        print('FAlta parametro')
        sys.exit(1)
    elif not sys.argv[1].isnumeric():
        print('FAlta parametro')
        sys.exit(1)

raio = sys.argv[1]
circulo(raio)

    
 

 



