from celery import Celery

job_queue = Celery("worker", broker="amqp://guest@queue//")

job_queue.conf.task_routes = {
    "job_queue.test": "main-queue",
    "files.process": "main-queue",
}


def create_index_file_job(file_id: str, s3_location: str):
    job_queue.send_task(
        "files.process",
        args=[file_id, s3_location],
    )
