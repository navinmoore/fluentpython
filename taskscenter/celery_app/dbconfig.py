# coding:utf-8

class ParentConfig:
    SQLALCHEMY_POOL_SIZE = 300
    SQLALCHEMY_POOL_RECYCLE = 900
    SQLALCHEMY_POOL_TIMEOUT = 900
    SQLALCHEMY_MAX_OVERFLOW = 50
    DB_URI = 'mysql+mysqlconnector://user:pwd@db_url/dbname'
    