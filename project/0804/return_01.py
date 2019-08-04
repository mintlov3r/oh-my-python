# return 提前结束，不会执行后面的语句，break，跳出循环


def func1(a, b):
    if a>b: # 互斥关系
        return 'nihao'
    return ''

def func2(a, b):
    if a>b:# 互斥关系
        return 'nihao'
    else:
        return 'ne'


def func3(a, b):
    if a>b: # 不是互斥关系
        print('nihao')
    print('enen')


def func4(a, b):
    if a>b: # 互斥关系
        print('niaho')
    else:
        print('enen')

print(func1())
