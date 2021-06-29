# Service A

Serviço desenvolvido em Python que faz integração com RabbitMQ mediante input de informações em front-end.

Para execução deste serviço deverá ser utilizado Docker conforme passos abaixo para criação dos containers.

----------------------------------------------------------------------------------------------
1- Criar container rabbitmq:

docker run -d --name rabbitmq -p 15672:15672 -p 5672:5672 rabbitmq:3-management

Acessar: http://localhost:15672/

-----------------------------------------------------------------------------------------------

2 - Criar container Serviço

Baixar Imagem Docker: docker pull rogeriol16/servicea

Criar container: docker run -d --name container_servicea -p 80:80 --link rabbitmq rogeriol16/servicea

Acessar via navegador: http://localhost/

-----------------------------------------------------------------------------------------------


Após subir os containers, poderá efetuar input via navegador de notificações que será entregue ao RabbitMQ.

Além do input, existe também a opção de Recuperar a notificação mediante ao ID inserido, assim este irá se conectar ao S3 AWS e verificar se existe a notificação desejada.

Documentação da API via Swagger: http://localhost/docs

OBSERVAÇÃO: Existe o serviço da outra ponta, onde captura as notificações no RabbitMQ e insere no S3 AWS que pode ser verificado atraves do repositório abaixo:

https://github.com/rogeriolopes16/ServiceB
