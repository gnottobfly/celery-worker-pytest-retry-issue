import os
from unittest.mock import Mock
from celery import Celery
import pytest

redis_url = os.environ.get("REDIS_URL", 'redis://localhost:6379/0')
app = Celery('test', broker=redis_url, backend=redis_url)

do_work = Mock()

@app.task(bind=True, max_retries=3, default_retry_delay=1)
def work_it(task):
    try:
        do_work()
    except Exception as e:
        raise task.retry(exc=e)

@pytest.fixture(scope='session')
def celery_config():
    return app.conf

def test_non_retry(celery_worker):
    work_it.delay().get(timeout=30)

def test_retries(celery_worker):
    do_work.side_effect = (Exception('Boom!'), None)
    work_it.delay().get(timeout=30)
