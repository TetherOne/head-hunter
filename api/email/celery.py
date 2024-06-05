from celery import Celery

celery = Celery(
    "email",
    broker="amqp://guest:guest@rabbitmq:5672",
    backend="rpc://",
)
