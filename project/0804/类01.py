class Stu:
    addr = ''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
    @staticmethod
    def dayin(x):# 不带self，附属于类，但和类没有关系
        print(x)

    @classmethod
    def dayin2(cls, x):# 带cls，类似于self，
        # 换了个名字用来显式指定为类的方法，附属于类可以直接调用
        print(x)

    def size(self):
        return self.length*self.width
    pass


s1 = Stu(name='ni', age=34)
print(s1)
Stu.dayin('ho')
s1.dayin('nihao')
Stu.dayin2('enen')
s1.dayin2('enen2')
