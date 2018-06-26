#coding=utf-8
"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def teleman(number,b,c,d):
    a = str(number)
    if a not in str(b) and a not in str(c) and a not in str(d):
        return number





txt_numbers = []
txt_bnumbers = []
call_numbers = []
call_bnumbers = []
telemarketers = []

for call in calls:
    call_numbers.append(call[0])
    call_bnumbers.append(call[1])
for text in texts:
    txt_numbers.append(text[0])
    txt_bnumbers.append(text[1])


for call_number in call_numbers:
    a = teleman(call_number, call_bnumbers,txt_bnumbers,txt_numbers)
    if a != None:
        telemarketers.append(a)

new_set = set(telemarketers)
# print new_set    

print ("These numbers could be telemarketers: \n{}".format("\n".join(sorted(new_set))))




"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

