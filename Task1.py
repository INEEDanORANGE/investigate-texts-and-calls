#coding=utf-8
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


count = 0
c = [item[0] for item in texts]
d = [item[0] for item in calls]
e = [item[1] for item in calls]
f = [item[1] for item in texts]
number = c + d + e + f
for i in set(number):
    count += 1
print ("There are {} different telephone numbers in the records.".format(count))

"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."""
