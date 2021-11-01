# coding:utf-8 
import datetime
from celery_app import app, ParentSession
from celery_app.sendmail import sendParentMail

@app.task
def parentPayment():
    session = ParentSession()
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=60)
    expect = (now + delta).strftime("%Y-%m-%d")
    sql = "select name from patents where payment = '{}'".format(expect)
    results = session.execute(sql)
    names = [result[0] for result in results]
    for name in names:
        sendParentMail.apply_async(args=(name,))
    return names
    