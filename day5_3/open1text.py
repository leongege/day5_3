#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"
# f1 = open("/root/passwd","r")
# print(f1.readline())
# f1.close()

# f2 = open("/root/passwd","r")
# for i in f2:
#     print(i.split(":")[0])
# f2.close()

f3 = open("/proc/meminfo","r")
for lines in f3 :
    if lines.startswith("MemTotal:"):
        memtotal = int(lines.split()[1]) / 1024 /1024
    if lines.startswith("MemFree:"):
        memfree = int(lines.split()[1]) / 1024 / 1024
        break
print("USED:%.2fG - %.2fG = %.2fG" %(memtotal,memfree,memtotal - memfree))
f3.close()

f4 = open("/proc/cpuinfo","r")
for i in f4:
    if i.startswith("cpu cores"):
        print(i.split(":")[1])
f4.close()


