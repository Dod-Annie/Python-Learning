# 为tuple中每个元素命名
## 定义一系列数值常量
NAME,AGE,SEX,EMAIL = range(4)

student = ('Jim',16,'male','jime@gmail.com')

print(student[EMAIL])

## 使用namedtuple代替tuple

from collections import namedtuple

Student = namedtuple('Student',['name','age','sex','email'])

s = Student('Jim',16,'male','jime@gmail.com') 

print(s.name) # 可以直接用属性访问tuple

print(isinstance(s,tuple) ) # namedtuple是tuple的子类
