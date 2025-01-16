import threading
import time

def main():
    th = threading.Thread(target=contar, args=('elefantes',10))
    th.start()
    print("Posso fazer outras coisas")

    th.join()
    print("Acabou tudo")

def contar(valor, repeticao):
    for x in range(1, repeticao +1):
        print(f'{x} {valor}')
        time.sleep(1)

if __name__ == "__main__":
    main()