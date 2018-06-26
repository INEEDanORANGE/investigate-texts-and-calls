#coding=utf-8
"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
#from pip._vendor.distlib._backport.tarfile import TUREAD

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def ban_num(a):
    if "(080)"in str(a):
        return True
    else:
        return False

def get_number(a):
    if "(" in str(a):
        d=get_code(a)
#         print d
        return d
    elif " " in str(a):
#         print a[0:4]
        return a[0:4]
    else:
        print (a)
        return a
def get_code(a): 
    co_num = ""
    for code in str(a):
        if code == "(":
            continue
        if code == ")":
            break
        else:
            co_num += code   
    return co_num

ban_calls = []
for call in calls:
    if ban_num(call[0]):
        ban_calls.append(call)
# print ban_calls    
        
list_code = []
for codes in ban_calls:
    list_code.append(get_number(codes[1]))
set_list_code = set(list_code)
new_list_code = "\n".join(sorted(set_list_code))
print ("The numbers called by people in Bangalore have codes: \n{}".format(new_list_code))
# print set(new_list_code)
total = 0
ban = 0
for codes in ban_calls:
    if ban_num(codes[1]):
        total += 1
        ban += 1
    else:
        total +=1
percentage = ( ban * 1.00  )/ total * 100

print("{:.2f}% percent of calls from fixed lines in Bangalore are calls \
to other fixed lines in Bangalore.".format(percentage))
"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
///找出被（080）xxxxxx呼叫的所有电话，提取出他们的区号和移动前缀
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。

BanCall = []
result = []
BanCallBan = []
#遍历calls中的号码：
for num in calls:
#对主叫号码进行条件判断
    if num[0][:5] == '(080)':
#收集符合条件的对应接听号码
        BanCall.append(num[1])
#遍历之前收集的号码
for eve in BanCall:
#对固定电话进行判断
    if eve[0] == '(':
#收集索引位置
        index = eve.find(')')
#对固定电话进行截取
        result.append(eve[1:index])
#对第二部分做准备
        if eve[:5] == '(080)':
            BanCallBan.append(eve)
#对移动号码进行判断
    if ' ' in eve:
#移动号码进行截取
        result.append(eve[:4])
#去重排序完成输出
print("\n".join(sorted(set(result))))
print("{:.2%} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format((len(BanCallBan) / len(BanCall))))
"""
