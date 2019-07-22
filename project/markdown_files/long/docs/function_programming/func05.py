# 闭包
# c语言函数可以嵌套使用的，但不可以嵌套
# python 可以嵌套定义
def a(ax):
    # ax变量
    def b():
        return ax+ax
    # 做了这一步，相当于在a里定义了一个“变量”b，但是她是一个函数，
    # 返回值就是a的变量的一个操作
    return b

print(a(4)())

def c(x):
    return x+x
# 函数名可以当变量调用，当函数名+()时，是调用
print(c)
def d(loop_num, func, handle_str):
    for i in range(loop_num):
        func(handle_str)

def f_print(s):
    print(s)

# d(9, f_print, 'nihao')

