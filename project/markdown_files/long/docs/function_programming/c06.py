def print_student_file(name, gender='男', age=18, collage='人民路小学'):
    print('我叫'+ name)
    print('我今年'+ str(age) + '岁')
    print('我是'+ gender + '生')
    print('我在' + collage + '上学')

# print_student_file('鸡小萌')

def f_a(c, rows=5):
    """
    rows打印几行
    可以指定打印行数，如果不指定默认打印5行
    """
    for i in range(rows):
        print(i+1, c)

# f_a('nihao')
f_a('nihao', 10)
print_student_file('123', age=18, collage='人民路小学')
# 赋值的必须写到后面

# f(a=9, 7, c=8)
# f(7, a=9, c=8)


# f = 2*x +7

def func(x, k=2 , b=7):
    return x*k+b
print(func(3))

# func(x=9, 8, b=10)
# print(func(8, x=9, b=10))
# 9*8+10
print(func(6))
print(func(k=8, b=10, x=9))

# 要处理某些大型数据，默认一次性处理100行，需要增大规模时，指定处理行数
# 100万行数据
def process(filename, read_chunksize=100):
    # 循环，每次读取100行，处理
    with open(filename, 'r') as f:
        f.readline()  # 读取一行
        # 读取一行
        # 读取一行
        # 。。。100行
        # 处理
        pass
        
        # 读取下一行

# 这个函数默认每次处理一百行，可以指定read_chunksize参数修改每次读取

def yici(x, k, b):
    return x*k+b
# 只要出现f(x=89, y=78, 89)，带等号一定要放到后面
# 不能重复传入参数，避免乱序，如果需要调整参数列表顺序，一定要指定变量名
# 

# print(yici( 4, 6, x=2))
print(yici(x=8, k=7, b=5))

# def f(b=56,a):
#     for i in range(a):
#         print(b)

# f(b=45, 3)
