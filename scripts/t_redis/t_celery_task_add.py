from scripts.celery_task.task1 import add
from scripts.celery_task.task2 import multi

# result = add(3,1)
# print(result)

# result1 = add.delay(2, 21)
# print(result1)
#
# result2 = multi.delay(4,6)
# print(result2)

from datetime import datetime,timedelta

# print(datetime.utcnow())
eta = datetime.utcnow() + timedelta(seconds=10)
add.apply_async(args=(200, 50), eta=eta)

