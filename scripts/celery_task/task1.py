from .celery import app


@app.task(name='scripts.celery_task.task1.add')
def add(x, y):
    print(x, y)
    return x + y
