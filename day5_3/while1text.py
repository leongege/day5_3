#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"
prompt = """qing1 a
qing2   b
qing3   c
"""
x = ""
while not x :
    print(prompt)
    x = int(input("xuanzedeshu"))
if x == 1:
    print("a")
elif x == 2:
    print("b")
elif x == 3:
    print("c")