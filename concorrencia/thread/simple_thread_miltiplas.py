import threading
import time

def main():
    lista = [threading.Thread(target=contar, args=('elefantes', 10)),
             threading.Thread(target=contar, args=('gafanhoto', 10)),
             threading.Thread(target=contar, args=('zina', 10)),
             threading.Thread(target=contar, args=('nene', 10)),
             threading.Thread(target=contar, args=('cabron', 10))

    ]
    [th.start() for th in lista]
    
    print("Posso fazer outras coisas")

    [th.join() for th in lista]
    
    print("Acabou tudo")

def contar(valor, repeticao):
    for x in range(1, repeticao +1):
        print(f'{x} {valor}')
        time.sleep(1)

if __name__ == "__main__":
    main()