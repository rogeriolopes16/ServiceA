import pika
import json
from minio import Minio

# funtion para envio de notificação ao RabbitMQ
def sendRabbitMQ(mensagem):
    try:
        if requestS3(mensagem["id"]) == 'Not Found':  # verifica se o id da notificação já existe cadastrada
            # envia notificação para fila do RabbitMQ
            credentials = pika.PlainCredentials('guest', 'guest')
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', credentials))
            channel = connection.channel()

            channel.queue_declare(queue='ServiceA')

            channel.basic_publish(exchange='',
                                  routing_key='ServiceA',
                                  body=json.dumps(mensagem),
                                  properties=pika.BasicProperties(
                                      delivery_mode=2,
                                  ))
            connection.close()
            return 'OK'
        else:
            return 'ID Existente'
    except:
        return 'Erro'

    # funtion recupera a notificação cadastrada no S3
def requestS3(id):
    try:
        # Create client with access and secret key.
        client = Minio("s3.amazonaws.com", "ACCESS-KEY", "SECRET-KEY")

        # Get object information.
        result = client.stat_object("serviceb", str(id))
        return {"id": result.metadata["x-amz-meta-id"], "notification": result.metadata["x-amz-meta-notification"]} # retorno caso seja true
    except:
        return "Not Found" # retorno caso seja false
