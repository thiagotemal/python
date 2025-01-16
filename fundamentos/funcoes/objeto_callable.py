#!/usr/bin/python3

from typing import Any


class area:
    def __init__(self, potencia):
        self.potenca= potencia
    
    def __call__(self, valor):
        return self.potenca ** valor
    
if  __name__ == '__main__':
    quadrado = area(2)

    if callable(area):
        print(f'valor calculado {quadrado(4)}' )
