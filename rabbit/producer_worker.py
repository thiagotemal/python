from typing import List
import pika
import time


def produce_messages(
    host: str, queue: str, exchange: str, message: List[str], routing_key: str
) -> None:
    """
    Publishes messages to a specified RabbitMQ exchange and queue.

    This function connects to RabbitMQ, declares a queue and an exchange, and 
    publishes messages to the specified exchange with a given routing key.

    :param host: The RabbitMQ server host.
    :param queue: The name of the queue.
    :param exchange: The name of the exchange.
    :param message: A list of messages to be sent.
    :param routing_key: The routing key for message delivery.
    :return: None
    """
    EXCHANGE_TYPE = "fanout"
    # Establish a connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host))
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue=queue)
    # Declare an exchange
    channel.exchange_declare(exchange=exchange, exchange_type=EXCHANGE_TYPE)

    # Publish each message in the list
    for m in message:
        channel.basic_publish(
            exchange=exchange,
            routing_key=queue,
            body=m,
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent,
            ),
        )
        print(f" [x] Sent {m}")
        time.sleep(1)  # Delay for demonstration purposes

    # Declare the queue again (it seems redundant, but kept as per original code)
    channel.queue_declare(queue=queue)

    # Example messages to be published
    messages = ["""Hello World!""", """Hello World 2!""", """Hello World 3!"""]

    # Publish example messages
    for message in messages:
        channel.basic_publish(
            exchange="",
            routing_key=routing_key,
            body=message,
            properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
        )
        print(" [x] Sent %r" % message)
        time.sleep(1)


def get_messages() -> List[str]:
    return ["Primeiro log", "Segundo log", "Terceiro log", "Quarto log", "Quinto log"]


if __name__ == "__main__":
    produce_messages("localhost", "queue_worker", "logs", get_messages(), "queue_worker")
