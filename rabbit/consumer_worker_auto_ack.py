import sys
import pika
import time


def consume_messages(host: str, queue: str) -> None:
    """Start consuming messages from queue_worker queue."""
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host)
    )
    channel = connection.channel()

    channel.queue_declare(queue=queue)

    def callback(ch, method, properties, body: bytes) -> None:
        print(" [x] Received %r" % body)
        time.sleep(body.count(b"."))
        print(" [x] Done")

    channel.basic_consume(
        queue=queue, on_message_callback=callback, auto_ack=True
    )


    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        consume_messages("localhost", "queue_worker")
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit(0)
