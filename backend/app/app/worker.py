from raven import Client

from app.services.job_queue import job_queue
from app.core.config import settings

client_sentry = Client(settings.SENTRY_DSN)


@job_queue.task(name="job_queue.test", acks_late=True)
def test_celery(word: str) -> str:
    return f"test task return {word}"
