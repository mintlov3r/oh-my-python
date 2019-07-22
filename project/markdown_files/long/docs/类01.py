import re
class Dog(object):

    pass

class Cat:
    pass

# 面向对象，面向过程
# 做一件事，公司的管理，管理人，管理事情，
# 分配任务，面向过程，拆分成子任务
# 面向对象
# 处理一份数据，输入，处理，输出

def in_function():
    pass

def process_function():
    pass

def output_function():
    pass

class Handler:
    """
    状态信息，属性，颜色，名字，状态，尺寸
    行为信息，方法，函数，吃，喝，跑
    """
    # def __init__(self, filename):
    #     self.filename = filename
    
    def input_function(self, filename):
        self.fob = open(filename)
        # return open(filename)
    
    def process_function(self):

        s = self.fob.readlines()
        self.fob.close()
        # 列表推导
        t = []
        for i in s:
            t.append(re.sub('\d', '', i))
        # return t
        self.t = t

    def output_function(self, target_filename):
        # print(content)
        with open(target_filename, mode='w') as f:
            f.write(''.join(self.t))
            print('写入成功')

    @staticmethod
    def bark():
        print('wangwang!\n')

    @classmethod
    def hello(cls):
        print(cls.__name__)

    def heihei(self):
        print(self)

# 读入一个文件，并删除每行记录的数字
handler = Handler()  # 初始化一个实例
# handler.input_function('./123.txt')
# handler.process_function()  # 实例方法，self，实例化方法使用前必须初始化一个实例
# handler.output_function('./29879342.txt')
# handler.bark()  # 静态方法，不需要初始化实例，也可以初始化使用
# Handler.bark()
# Handler.hello()  # 不需要初始化实例，也可以初始化使用
handler.heihei()
