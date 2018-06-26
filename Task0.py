
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

number = texts[0]
num = calls[-1]

print ("First record of texts,{} texts {} at time {}".format(number[0],number[1],number[2]))
print ("Last record of calls,{} calls {} at time {}, Lasting {} seconds".format(num[0],num[1],num[2],num[3]))


