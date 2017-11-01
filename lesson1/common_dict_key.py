# 快速找到多个字典中的公共键
from random import randint,sample

from functools import reduce

## 随机产生一个List
print(sample('abcdefg',randint(3,6))) 

s1 = {x: randint(1,4) for x in sample('abcdefg',randint(3,6)) }

s2 = {x: randint(1,4) for x in sample('abcdefg',randint(3,6)) }

s3 = {x: randint(1,4) for x in sample('abcdefg',randint(3,6)) }

print(s1,s2,s3)

## 找出s1,s2,s3的公共键

d = map(dict.keys, [s1,s2,s3])

print(list(d))

# 使用reduce函数

print(reduce(lambda a,b: a & b,map(dict.keys, [s1,s2,s3])))
