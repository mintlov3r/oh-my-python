# 匿名函数和map、reduce经常连用
# map，映射，可以理解为集合中的象集和集，
# 自变量和因变量的对应关系，(匿名函数或是函数)但是有区别
# 函数是多对一或一对一，一个自变量只能对应一个因变量，
# 多个自变量可能对应一个因变量
# f(x1) = f(x2) = y    (x1 不一定等于 x2)
# reduce 减少，怎么减少，利用某种方式(匿名函数或函数)

def f(x):
    """
    y = f(x) = x^2
    """
    return x-3

f2 = lambda x: x**3
input_list = list(range(10))
s = map(f2, input_list)
print(input_list)
print(list(s))


s3 = list(map(lambda x: x**3, list(range(10))))
print(s3)   