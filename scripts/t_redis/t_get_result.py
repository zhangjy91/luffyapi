from scripts.celery_task.celery import app

from celery.result import AsyncResult

id = '9805a57f-d796-4f99-bf29-42f9f45f58ea'
#
# if __name__ == '__main__':
#
#     async = AsyncResult(id=id,app=app)
#     # async = AsyncResult(id=id, app=app)
#     if async.successful():
#         result = async.get()
#         print(result)
#
#     else:
#         print('没拿到结果')