# 统计序列中元素的出现频度
from random import randint 

data = [randint(0,20) for _ in range(30)]

c = dict.fromkeys(data,0)

for x in data:
    c[x] += 1

print(c)

# 根据字典的值对字典进行排序
##使用collections的Counter对象
from collections import Counter

c2 = Counter(data) # c2[value]可以用来统计字典相同value数量

print(c2)

## most_common方法接受一个len，返回频数最高的前len项
print(c2.most_common(3))
