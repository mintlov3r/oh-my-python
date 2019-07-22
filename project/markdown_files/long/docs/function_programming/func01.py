# 匿名函数
f = lambda x: x+2
# 等价于，可扩展
def f2(x):
    # print(x)
    return x+2
# 等价于
# def f3(x): return x+2

print('匿名函数f=', f(2))
print('普通函数f2=', f2(2))