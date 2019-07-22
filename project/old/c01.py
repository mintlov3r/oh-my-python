import os

filepath = './nihao'

if not os.path.exists(filepath):
    os.mkdir(filepath)
else:
    print('exists')
# os.removedirs('./myfolder')


# os.path.


# 创建一个空文件

filename = './good.txt'
with open(filename, mode='a+',encoding='utf-8') as fw:
    fw.write('今天真好啊!哈哈哈哈\n')


order_list = list(range(1, 23))

# for(i=1;i<=10;i++){
#     fucn(i)
# }

# 遍历
for i in range(1, 10):
    print(i, end=', ')

print()
a = "10"
b = '10'
a = int(a)

a = 89
def func(a, b=10):
    print(a, b)

func('34','78')

# void func2(int n, double b){

# }

if a == 10:
    print('a是数字')
else:
    print('a不是数字')

if a == b:
    print('a=b')
else:
    print('a<>b')
# 字典，集合

print()
print('-'*100)
print(range(2, 9))

# a = 1
# b = 2
