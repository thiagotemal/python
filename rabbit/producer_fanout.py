from ast import List

import pika

def readFile() -> List:
    with open('log.txt') as f: 
        listaLinhas = []
        formated=  f.read().splitlines("")
        for line in formated:
            zibna = line.strip().split(" ")
            if  len(zibna)  > 2:
                listaLinhas.append(({"level":zibna[2], "message": line}))
         

            
      
    return listaLinhas

def sendToQueue(listaLinhas: List, host: str, exchangeName :str) -> None:
    if  listaLinhas:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        channel = connection.channel()
        channel.exchange_declare(exchange=exchangeName, exchange_type='fanout')

        for line in listaLinhas:        

            channel.basic_publish(exchange='logs', routing_key=line["level"], body=line["message"])
            print(f"[x] Sent line {line}")
        
        print("Lines sented")

        connection.close()


if __name__ == "__main__":
    sendToQueue(readFile(), 'localhost', 'logs')

    