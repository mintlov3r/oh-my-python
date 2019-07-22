# 零除错误
# 假如说遇到错误，希望程序能够提示，正常运行不中断，或者处理异常

while True:
    try:
        print('-'*20)
        a = eval(input("请输入一个数字当做分母：\n"))
        b = eval(input("请输入一个数字当做分子：\n"))
        print('计算结果是：{}\n'.format(b/a))
        c = eval(input("请输入是否要终止\n0-终止，1-继续\n"))
        if c == 0:
            break
    except Exception as e:
        print('{}-好像哪里不太对，请重试！\n'.format(e))
        # 可以在这里进行处理