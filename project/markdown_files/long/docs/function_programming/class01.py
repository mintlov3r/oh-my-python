class Student:
    # def 
    pass
# y = x**2*a

# 函数是一个类似于黑盒的东西，有零个或多个输入，有零个或多个输出
# 函数编程，锤子，工具


# int main(void){
#     printf("hello!\n");
#     return 0;
# }

def f(x, y):
    return x+y

# 输入-输出
# n可能是1一个或多个
# 0-0
# 0-n
# n-0
# n-n

def f2():
    x= 89
    y =78
    return x, y
print(f2())

def f3(x, y, z):
    print(x)
    print(y)
    print(z)

f3(6, 8, 9)


# 变长参数
x, *args= f2()
print(args)
# 解包

def print_hello():
    print("hello!\n")
    # 打一顿仇人

def kick():
    # 打仇人
    pass
