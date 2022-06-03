from celery import Celery

# 加载django环境
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "luffyapi.settings.dev")
django.setup()

broker = 'redis://127.0.0.1:6379/1'
backend = 'redis://127.0.0.1:6379/2'

app = Celery(__name__, broker=broker, backend=backend, include=['celery_task.home_task'])

app.conf.timezone='Asia/Shanghai'
app.conf.enable_utc=False

from datetime import timedelta
from celery.schedules import crontab

app.conf.beat_schedule = {
    'add_task':{
        'task':'celery_task.home_task.banner_update',
        'schedule':timedelta(seconds=30),
        # 'schedule': crontab(hour=8, day_of_week=1), #每周一早上8点
        # 'args':(300,150), #每次执行一次, 300 + 150
    }
}

#一定要启用beat，来执行定时任务
# celery beat -A celery_task -l info
