#!/usr/bin/python3

def generator():
    contador = 0
    while(True):
        contador+=1
        yield contador
    

if __name__ == "__main__":
    seq = generator()
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))

    