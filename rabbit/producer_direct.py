from typing import List
import pika


def read_file() -> List:
    with open("log.txt") as f:
        lista_linhas = []
        formated = f.read().splitlines("")
        for line in formated:
            zibna = line.strip().split(" ")
            if len(zibna) > 2:
                lista_linhas.append(
                    ({"level": zibna[2], "message": line})
                )

    return lista_linhas


def produce_messages(
    lista_linhas: List, host: str, exchange: str
) -> None:
    if lista_linhas:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host)
        )
        channel = connection.channel()
        channel.exchange_declare(
            exchange=exchange, exchange_type="direct"
        )

        for line in lista_linhas:
            channel.basic_publish(
                exchange=exchange,
                routing_key=line["level"],
                body=line["message"],
            )
            print(f"[x] Sent line {line}")

        print("Lines sented")

        connection.close()


if __name__ == "__main__":
    produce_messages(read_file(), "localhost", "direct_logs")
