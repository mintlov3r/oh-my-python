class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    @property
    def volumn(self): # 不能传值，标注是一个属性，而非方法
        return self.length*self.width*self.height


b = Box(20, 40, 67)
print(b.volumn)
