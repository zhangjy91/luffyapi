from celery import Celery

backend = 'redis://127.0.0.1:6379/4'
broker = 'redis://127.0.0.1:6379/3'

app = Celery(__name__, broker=broker, backend=backend)


@app.task(name='t_celery_task.add')
def add(x, y):
    print(x, y)
    return x + y
