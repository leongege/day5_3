#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"
l1 = [1,2]
num = int(input("num:"))
for i in range(num -2):
    l1.append(l1[-1] + l1[-2])
print(l1)