# coding:utf-8 

from celery_app.workParent import parentPayment

# taskA.apply_async(args=[1, 2])

result = parentPayment.apply_async()
print(dir(result))
print(result.result)
# print("here")