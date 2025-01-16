#!/usr/bin/python3
from math import pi
import sys

def circulo(area):
    print('Area do Circulo ', pi * float(area) ** 2)
    

if __name__=='__main__':
    if len(sys.argv) <2:
        print('FAlta parametro')
    else:        
        raio = sys.argv[1]
        circulo(raio)
    
 

 



