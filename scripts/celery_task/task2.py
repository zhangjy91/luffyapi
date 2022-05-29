from .celery import app

@app.task(name='scripts.celery_task.task2.multi')
def multi(x, y):
    print(x, y)
    return x * y
