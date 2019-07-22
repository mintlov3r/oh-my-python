# 高阶函数
def f(x):
    return x**3

def f2(x):
    return x-9

def add(x, y, f):
    return f(x)+f(y)

# 一个加数加上另一个加数，等于和

print(add(8,7,f))
print(add(89, 90, f2))
