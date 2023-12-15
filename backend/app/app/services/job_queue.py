from celery import Celery

job_queue = Celery("worker", broker="amqp://guest@queue//")

job_queue.conf.task_routes = {"job_queue.test": "main-queue"}
