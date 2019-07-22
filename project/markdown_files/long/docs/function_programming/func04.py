# reduce减少某种
# # 
# d = {
#     'a': 1,
#     'b': 2,
# }
# print(d)

# e = dict(f=9,h=10)
# print(e)
# 大型任务，计算袋子个数，几个人一起算
# 切片，分配任务
# 计数，map

# 黄色 100 绿色200 
# 蓝色56 白色34 
# 黄色42 绿色242 
# 紫色67 黑色23

# 要按颜色合计 reduce
# 黄色。。 蓝色。。。 白色。。
from functools import reduce
f = lambda x, y: x+y

def f2(x, y):
    r = x*y
    return r
l = list(range(1,11))
l_2 = [1, 2]
r = reduce(f2, l)
print(r)

