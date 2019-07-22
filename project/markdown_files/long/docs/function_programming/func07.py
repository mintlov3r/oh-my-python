# 装饰器
"""
实现一个功能，记录函数的打印日志
写了一个大型工程，想知道运行过程中，调用了那些函数
1、对于每个用到的函数，都去修改执行内容（增加写入日志模块）
2、利用装饰器
"""
import time
import datetime
# def log(func):
#     # args arguments
#     # keyword arguments
#     def wrapper(*args, **kwargs):
#         # 增加的执行内容
#         print('正在执行的函数是:-', func.__name__)
#         with open('log.txt', mode='a', encoding='utf-8') as f:
#             f.write('正在执行的函数是:-\t{}\t{}\n'.format(datetime.datetime.now(), 
#                 func.__name__))
#         # 这一句类似于处理，替换成其他操作，例如写入日志文件
#         return func(*args, **kwargs)
#     return wrapper




# @log
# def now():
#     print(datetime.datetime.now())

# @log
# def happy():
#     pass

# now()
# happy()


# @log
# def func3():
#     print('hello!\n')

# # func3 = log(func3) = wrapper
# 名字没变，但是含义已经发生变化
# func3(7, 8) = wrapper(7, 8)

def log2(func):
    # args arguments
    # keyword arguments
    # *a **kw 代表接收任意参数，并保存下来供以后使用
    # *a []
    # **kw {'x': 8}

    # def f(8, 89, x=90, y=100):
    #     *a = [8, 89]
    #     **kw = {'x': 90,
    #             'y': 100
    #     }
    #     接收了参数列表中的所有值

    def wrapper(*args, **kwargs):
        # 增加的执行内容
        print('正在执行的函数是:-', func.__name__)
        with open('log.txt', mode='a', encoding='utf-8') as f:
            f.write('正在执行的函数是:-\t{}\t{}\n'.format(datetime.datetime.now(), 
                func.__name__))
        # 这一句类似于处理，替换成其他操作，例如写入日志文件
        func(*args, **kwargs)
        print('执行完了！\n')
        # return func(*args, **kwargs)
    return wrapper


@log2
def a():
    # print('正在运行a')
    pass
@log2
def b():
    # print('正在运行a')
    pass
@log2
def c():
    # print('正在运行a')
    pass
@log2
def d():
    # print('正在运行a')
    pass



a()
b()
c()
d()