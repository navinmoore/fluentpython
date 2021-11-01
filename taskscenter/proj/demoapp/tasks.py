# coding:utf-8
import time
from celery import shared_task
from celery import Task
# from demoapp.models import Widget

@shared_task
def add(x, y):
    print("shared_task_add:{0}+{1}={2}".format(x, y, x+y))
    return x + y


@shared_task
def mul(x, y):
    print("shared_task_mul:{0}*{1}={2}".format(x, y, x*y))
    return x * y

@shared_task
def xsum(numbers):
    print("shared_task_sum:{}".format(numbers))
    return sum(numbers)


@shared_task
def count_widgets():
    return Widget.objects.count()


# @shared_task
# def rename_widget(widget_id, name):
#     w = Widget.objects.get(id=widget_id)
#     w.name = name
#     w.save()


# class CourseTask(Task):
#     name = "course_task"

#     def run(self, *args, **kwargs):
#         print('start course task')
#         time.sleep(4)
#         print('args={}, kwargs={}'.format(args, kwargs))
#         print('end course task')
#         return self.name