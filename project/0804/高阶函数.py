from functools import reduce
def is_number(x):
    if isinstance(x, int) or isinstance(x, float) or x.isdigit():
        return True
    return False

# map, reduce, filter 组合可以使用推导式进行代替（官方推荐）

lst = list(range(10))+list('nihao')
print(lst)
# 实现每个元素的处理
lst2 = list(map(lambda x:x*2, lst))
print(lst2)
lst3 = [x*2 for x in lst]
print(lst3)
# 实现每个元素的处理并过滤
# 先过滤出所有数字，然后进行后处理
lst4 = list(map(lambda x:x*2, list(filter(is_number, lst))))
# print(list(filter(is_number, lst)))
print(lst4)

lst5 = [x*2 for x in lst if is_number(x)]

print(lst5)
# print(is_number(78.90))

# reduce

# 传递一个聚合函数，传递一个列表
# 对列表的所有数值进行聚合
# print(sum(list(range(5))))

def total(x, y):
    return x+y
print(reduce(total, lst5))
print(sum(lst5))