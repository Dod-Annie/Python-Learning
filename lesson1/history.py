# 实现历史记录功能
from collections import deque

q = deque([],5)

q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.append(6)

print(q)

import pickle # 可以将一个python对象存储进文件

pickle.dump(q,open('history'),'w')

q2 = pickle.load(open('history'))

print(q2)