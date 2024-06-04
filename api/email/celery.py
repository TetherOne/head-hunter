from celery import Celery


celery = Celery(
    "tasks",
    broker="amqp://guest:guest@rabbitmq:5672",
    backend="rpc://",
)
