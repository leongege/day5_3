#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"
# sum = 0
# for i in range(0,101):
#     sum += i
# print(sum)
# for i in range(1,101):
#     if i % 2 == 0:
#         sum +=i
# print(sum)
# for i in range(1,101):
#     if i % 2 == 1:
#         sum +=i
# print(sum)
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%s x %s = %s" %(j,i,j * i),end = "  ")
#     print()
l1 = [0,1]
for i in range(2  ,9):
    l1.append(l1[-1] + l1[-2])
print(l1)