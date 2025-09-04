class Person:
    name = None
    age = None
    def set_name(self):
        self.name = input('请输入姓名:')
    def set_age(self):
        self.age = input('请输入年龄:')
    def get_name(self):
        if self.name:
            return self.name
        else:
            print('无')
    def get_age(self):
        if self.age:
            return self.age
        else:
            print('无') 
p = Person()
p.get_age()

class Rectangle:
    length = None
    width = None
    def set_length(self):
        self.length = float(input("请输入矩形的长度："))
    def set_width(self):
        self.width = float(input("请输入矩形的宽度："))
    def get_primeter(self):
        if not self.length: #返回True执行if
            self.set_length()
        if not self.width:
            self.set_width()
        return (self.width + self.length) * 2
r = Rectangle()
r.get_primeter()