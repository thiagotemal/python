from sys import argv
import pika


def consumer(
    host: str, exchange: str, callback: callable, level=""
) -> None:
    """
    Connects to RabbitMQ and consumes messages from a fanout exchange.

    This function declares a fanout exchange and a random queue, binds the queue to the exchange, and starts consuming from the queue. It will call the callback function on each message received.

    :param host: The host to connect to.
    :param exchangeName: The name of the fanout exchange to connect to.
    :param callback: The callback function to call on each message received.
    :return: None
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host)
    )
    channel = connection.channel()

    channel.exchange_declare(
        exchange=exchange, exchange_type="direct"
    )

    result = channel.queue_declare(queue="", exclusive=True)

    queue_name = result.method.queue

    channel.queue_bind(
        exchange=exchange, queue=queue_name, routing_key=level
    )

    print(" [*] Waiting for logs. To exit press CTRL+C")
    try:
        channel.basic_consume(
            queue=queue_name,
            on_message_callback=callback,
            auto_ack=True,
        )

        channel.start_consuming()

    except KeyboardInterrupt:
        print("Interrupted")
        channel.stop_consuming()


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


if __name__ == "__main__":
    if argv :
        match argv[1:]:
            case "DEBUG":
                consumer("localhost", "direct_logs", callback, "DEBUG")
            case "INFO":
                consumer("localhost", "direct_logs", callback, "INFO")
            case _:
                consumer("localhost", "direct_logs", callback)
