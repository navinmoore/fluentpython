# coding:utf-8
from datetime import timezone
from celery.schedules import crontab

timezone = "Asia/Shanghai"
broker_url = 'pyamqp://guest:guest@127.0.0.1:5672//'
accept_content = ['json']
# result_backend = 'db+mysql://apl:Apl123456@rm-2ze9uiue6mo09e0m9o.mysql.rds.aliyuncs.com:3306/proj'
result_backend = 'django-db'
task_serializer = 'json'

# CELERY_RESULT_BACKEND = 'django-db'

beat_schedule = {
    "add-every-300-seconds": {
        'task': "demoapp.tasks.add",
        'schedule': 300.0, # 每隔300s执行一次任务
        'args': (2, 8),
    },
    "add-every-day": {
        "task": "demoapp.tasks.mul",
        "schedule": crontab(hour=17, minute=50), # 每天12点10分执行
        "args": (12, 18),
    }
}
