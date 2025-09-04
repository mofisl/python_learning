class Meet:
    nums = 0
class Egg(Meet):
    name = "鸡蛋"
    price = 1
class Beef(Meet):
    name = "牛肉"
    price = 25
class Mutoon(Meet):
    name = "羊肉"
    price = 30
class Vegetable:
    nums = 0
class Onion(Vegetable):
    name = "洋葱"
    price = 2
class Tomato(Vegetable):
    name = "番茄"
    price = 2
class Potato(Vegetable):
    name = "土豆"
    price = 3
class Radish(Vegetable):
    name = "萝卜"
    price = 3
class Menu:
    def order(self):
        print('吃什么')
        self.x = []
        dishes = input("1.洋葱炒牛肉；2.洋葱炒羊肉；3.煎蛋；4.番茄炒蛋；5.土豆萝卜炖羊肉。请输入数字空格分隔")
        dishes = dishes.split()
        while dishes:
            dish = dishes.pop(0)
            if dish == '1':
                onion = Onion()
                onion.num = 1
                beef = Beef()
                beef.num = 1
                self.x.extend([onion, beef])
            if dish == '2':
                onion = Onion()
                onion.num = 1
                mutoon = Mutoon()
                mutoon.num = 1
                self.x.extend([mutoon, onion])
            if dish == '3':
                egg = Egg()
                egg.num = 2
                self.x.append(egg)
            if dish == '4':
                tomato = Tomato()
                tomato.num = 2
                egg = Egg()
                egg.num = 3
                self.x.extend([tomato, egg])
            if dish == '5':
                potato = Potato()
                potato.num = 2
                radish = Radish()
                radish.num = 1
                mutoon = Mutoon()
                mutoon.num = 2
                self.x.extend([potato, radish, mutoon])
    def pay(self):
        total = 0
        for each in self.x:
            print(each.name, each.price, "*", each.num)
            total += each.price * each.num
        print(f"感谢惠顾，您一共消费了 {total} 元，欢迎下次光临~")
menu = Menu()
menu.order()
menu.pay()