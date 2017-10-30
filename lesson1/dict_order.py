#根据字典中值的大小，对字典的项排序
##内置函数sorted
sorted([9,1,2,8,5])

from random import randint

d = {x: randint(60,100) for x in 'xyzabc'}

print(sorted(d)) #对字典使用sorted会直接对键排序

# 将dict转化成tuple

## 使用zip函数

s = zip(d.values(),d.keys())  

print(sorted(s))

## 使用sorted函数中的Key参数

s2 = sorted(d.items(), key=lambda x: x[1])

print(s2)