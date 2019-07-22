class Dog:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def get_color(self):
        print(self.color)

dog = Dog(name='dahuang', color='yellow', size='L')
dog.get_color()

# 结构体struct


class Cat:
    color = 'red'
    name = 'xiaohei'
    size = 's'

print(Cat.color)

# 继承
class Samo(Dog):
    def get_size(self):
        print(self.size)

s = Samo(name='laobai', color='white', size='M')
s.size = 'L'
s.get_size()
