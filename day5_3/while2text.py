#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"

name = input("uname")
password = input("pswd")
sum = 0
while True:
    if name == "tom" and password == "123":
        print("successful")
        break
    else:
        sum += 1
        print("shibaicishu%s" %sum)
        name = input("uname")
        password = input("pswd")
    if sum == 2:
        print("shibai %s false" %(sum + 1))
        break
