#! /usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Fengxuewei"
# Date: 2020/6/21


# 1、列表解析
############################################################################################
data = [1, 5, 3, 2, 0, 6, 9]
res = []
for x in data:
    if x > 0:
        res.append(x)

print(res)


from random import randint
data = [randint(-10, 10) for _ in range(10)]
print(data)

new_data = filter(lambda x: x >= 0, data)
print(list(new_data))


new_data = [x for x in data if x >= 0]
print(list(new_data))


#  map()
# 遍历序列，对序列中每个元素进行操作，最终获取新的序列。
li = [11, 22, 33]
sl = [1, 2, 3]
new_list = map(lambda a, b: a + b, li, sl)
print(list(new_list))


#  reduce()
#  对于序列内所有元素进行累计操作
from functools import reduce
li = [11,22,33]
result = reduce(lambda a,b:a+b,li)
# reduce的第一个参数，函数必须要有两个参数
# reduce的第二个参数，要循环的序列
# reduce的第三个参数，初始值
print(result)


#  filter()
#  对于序列中的元素进行筛选，最终获取符合条件的序列
li = [11,22,33]
new_list = filter(lambda a:a>22,li)
print(list(new_list))
#filter第一个参数为空，将获取原来序列



## 2、字典解析
###################################################################################################
d = {x:randint(60,100) for x in range(1,21)}
print(d)

new_d = { k : v for k, v in d.items() if v > 90 }
print(new_d)




# 3、集合解析
#############################################################################################################
#列表转集合的方式
data=[1,5,3,2,0,6,9]
s = set(data)
print(s)


new_s = {x for x in s if x>=3}
print(new_s)