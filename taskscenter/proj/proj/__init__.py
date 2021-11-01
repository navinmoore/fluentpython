# coding:utf-8

from .celery import app as celery_app
'''
Python中一个py文件就是一个模块，“__all__”变量是一个特殊的变量，可以在py文件中，也可以在包的__init__.py中出现。
在模块中的__all__变量就是为了限制或者指定能被导入到别的模块的函数，类，全局变量等，
如果指定了那么只能是指定的那些可以被导入，没有指定默认就是全部可以导入，当然私有属性应该除外。
'''
__all__ = ("celery",)