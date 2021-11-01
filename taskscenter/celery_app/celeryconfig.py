# coding:utf-8
from kombu import Exchange, Queue
from datetime import timedelta, timezone
from celery.schedules import crontab

# BROKER_URL = "redis://47.106.106.220:5000/1" 
# CELERY_RESULT_BACKEND = "redis://47.106.106.220:5000/2"

# broker_url = "pyamqp://guest@127.0.0.1//"
broker_url = "pyamqp://guest:guest@rabbit//"
result_backend = "redis://redis"
timezone = "Asia/Shanghai"

imports = ("celery_app.tasks", "celery_app.workParent", "celery_app.sendmail")

beat_schedule = {
    # "add-every-30-seconds": {
    #     'task': "celery_app.tasks.schedule",
    #     'schedule': 300.0, # 每隔10s执行一次任务
    #     'args': (2, 8),
    # },
    "add-every-monday-morning": {
        "task": "celery_app.workParent.parentPayment",
        "schedule": crontab(hour=14, minute=10), # 每天12点10分执行
        "args": (),
    }
}


# task_queues = (
#     Queue(name="default", exchange=Exchange("default"), routing_key="default"),
#     Queue(name="for_task_A", exchange=Exchange("for_task_A"), routing_key="for_task_A"),
#     Queue(name="for_task_B", exchange=Exchange("for_task_B"), routing_key="for_task_B"),
# )

# task_routes = {
#     'tasks.taskA':{"queue":"for_task_A","routing_key":"for_task_A"},
#     'tasks.taskB':{"queue":"for_task_B","routing_key":"for_task_B"}
# }


