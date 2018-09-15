#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"
"""function1

+ - * /
"""
#yunsuan
def fun1(x,y):
    "Usage:+"
    return "%s + %s = %s" % (x, y, x + y)
def fun2(x,y):
    "Usage:-"
    return "%s - %s = %s" % (x, y, x - y)
def fun3(x,y):
    "Usage:*"
    return "%s * %s = %s" % (x, y, x * y)
def fun4(x,y):
    "Usage:/"
    return "%s / %s = %s" % (x, y, x / y)
if __name__ == "__main__":
    print(fun1(1,2))
    print(fun2(4,2))