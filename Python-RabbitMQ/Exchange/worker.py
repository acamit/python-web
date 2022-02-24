import pika, sys, os, time

def main():
    # connected to a broker on localhost, add IP address for remote server.
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True) # no harm in declaring again

    def callback(ch, method, properties, body):
        print("[x] Received %r" % body.decode())
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag= method.deliver_tag)
    
    # dont recieve more than 1 message until that one is acknowledged back
    channel.basic_qos(prefetch_count=1)
    # tell pika that callback method should consume messages from rabbit mq
    channel.basic_consume(queue='hello', on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)