#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"
import sys
try:

    f1 = open("/root/aaa.txt","r")
    for i in f1:
        print(i)
except NameError as e:
    print(e,"not found,   again")