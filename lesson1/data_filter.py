# 在列表 字典 集合中根据条件筛选数据
# 列表
## filter函数
from random import randint

data = [randint(-10, 10) for _ in range(10)]#py3:range;py2:xrange

data1 = filter(lambda x: x>=0, data)

# print(list(data1))

##列表解析

print([x for x in data if x>= 0]) #推荐使用列表解析

#字典

d = {x: randint(60,100) for x in range(1,21)}

print(d)

##字典解析

print({k:v for k,v in d.items() if v > 90})#py3:items;py2:iteritems

##集合解析

s = set(data)

print({x for x in s if x%3 ==0})