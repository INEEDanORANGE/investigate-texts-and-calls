#coding=utf-8
import csv
# from curses.has_key import has_key
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

a={}

for call in calls:
    number_one = call[0]
    number_two = call[1]
    time = int(call[3])
    if a.get(number_one)==None:
        a[number_one] = time
        if a.get(number_two)==None:
            a[number_two] = time
        else:
            a[number_two] += time
    else:
        a[number_one] += time
        if a.get(number_two)==None:
            a[number_two] = time
        else:
            a[number_two] += time

# print a
# c = 0
# d = ''
# for big in a:
#     if a.get(big) >= c:
#         c = a.get(big)
#         d = big
#
b = sorted(a.items(),key=lambda x:x[1],reverse=True)


print ("{} spent the longest time, {} seconds, on the phone during September 2016".\
       format(b[0][0],b[0][1])\
       )




'''
coding=utf-8
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
'''
