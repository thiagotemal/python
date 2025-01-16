import sys
import pika
import time


def consume_messages(host: str, queue: str) -> None:
    """
    Connects to RabbitMQ, declares a durable queue, and starts consuming messages from the queue.

    The callback function prints the message body, sleeps for the number of dots in the message, and acknowledges the message.

    :param host: The hostname or IP address of the RabbitMQ server.
    :param queue: The name of the queue to consume from.
    :return: None
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters(host))
    channel = connection.channel()

    channel.queue_declare(queue=queue)

    def callback(ch, method, properties, body):
        """
        The callback function to be called when a message is received from the queue.

        It prints the message body, sleeps for the number of dots in the message, and acknowledges the message.

        :param pika.Channel ch: The channel object.
        :param pika_SPEC.Basic.Deliver method: The method object.
        :param pika_SPEC.BasicProperties properties: The properties object.
        :param bytes body: The message body.
        :return: None
        """
        print(" [x] Received %r" % body)
        time.sleep(body.count(b"."))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue, on_message_callback=callback)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        consume_messages("localhost", "queue_worker")
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit(0)
            

