# coding:utf-8

from celery import Celery
from sqlalchemy import create_engine as create_default_engine
from sqlalchemy.orm import sessionmaker

from .dbconfig import ParentConfig

app = Celery("tasksCenter")
ParentSession = sessionmaker()

app.config_from_object("celery_app.celeryconfig")

print(ParentConfig.DB_URI, "here")

ParentSession.configure(bind=create_default_engine(ParentConfig.DB_URI, 
    pool_size=ParentConfig.SQLALCHEMY_POOL_SIZE, 
    pool_recycle=ParentConfig.SQLALCHEMY_POOL_RECYCLE, echo=False))



