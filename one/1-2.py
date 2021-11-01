# -*- coding:utf-8 -*-
# Author: your name
# Date: 2021-10-19 10:26:47
# LastEditTime: 2021-10-19 13:05:37
# LastEditors: Please set LastEditors
# Description: In User Settings Edit
# FilePath: /fluentpython/1-2.py
# 
"""
bool(x) 首先会调用__bool__() 如果没有，则调用__len__()
"""

from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """

        """
        return 'Vector(%r, %r)' % (self.x, self.y)
    
    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x*scalar, self.y*scalar)

    
if __name__ == '__main__':
    v = Vector('1', '2')
    print(v)

