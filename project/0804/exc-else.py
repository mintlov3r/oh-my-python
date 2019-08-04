# coding:utf-8
# 奖励机制


try: # 尝试进行
    1/0
    # print('enen')

except Exception as e:  # 如果出现指定的异常，执行
    # print(e)
    pass
else:  # 未出现异常的奖励
    print('success!')
finally:  # 无论前面发生什么情况，都要执行，数据库关闭，文件关闭
    print('结束啦！')

with open('1.txt', mode='r')as f:
    print(f.read())


try:
    f = open('1.txt', mode='r') # 打开一个文件，把文件句柄（指针）给f
    print(f.read())
except Exception as e: # 如果出现异常，会pass
    pass
finally: # 进行关闭f
    f.close()


# try:
#     print('-'*20)
#     a = eval(input("请输入一个数字当做分母：\n"))
#     b = eval(input("请输入一个数字当做分子：\n"))
#     print('计算结果是：{}\n'.format(b/a))
#     c = eval(input("请输入是否要终止\n0-终止，1-继续\n"))
#     if c == 0:
#         break
# except Exception as e:
#     print('{}-好像哪里不太对，请重试！\n'.format(e))
#     # 可以在这里进行处理