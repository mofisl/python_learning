'''
继承也必须传参数：
    1、super().__init__() 要把父类需要的参数补齐
    2、self 只是对象本身的引用
    class SportCar(Automobile):
    def __init__(self, *args, damage, **kwargs):
        super().__init__(*args, **kwargs)   # 自动把父类的参数传进去
        self.damage = damage
首先是车类
然后每个子类继承，同样多态性，租金变化。
管理理类，内部分工不同函数
设置字典储存每辆车信息，用dict.get(key)进行判断
    如果用户输入的 carid 不存在：
    .get(carid) → None
if None: → 条件为 False
再设置分类字典储存分类车信息
分类字典的value是实例对象，是一个list储存起来的
    self.cars = {} —— 快速查找（通过车ID）
    self.stocks = {...} —— 分类存储（方便展示和管理）
'''
class Automobile:
    def __init__(self, brand, model, platenum, dayrent, carid):
        self.brand = brand          # 品牌
        self.model = model          # 型号
        self.platenum = platenum    # 车牌
        self.rent = dayrent         # 租金（每天）
        self.carid = carid          # 车辆编号
    def get_brand(self):
        return self.brand
    def get_model(self):
        return self.model
    def get_platenum(self):
        return self.get_platenum
    def get_dayrent(self):
        return self.rent
    def get_carid(self):
        return self.carid
    def calc_rent(self, days, discount=1):#discount折扣
        return self.rent * days
class EconomyCar(Automobile):
    def __init__(self, brand, model, platenum, dayrent, carid, subsidy):
        super().__init__(brand, model, platenum, dayrent, carid)
        self.subsidy =subsidy
    def get_subsidy(self):
        return self.subsidy
    def calc_rent(self, days, discount=1):#discount折扣
        return super().calc_rent(days, discount=1) - self.subsidy * days
class LuxuryCar(Automobile):
    def __init__(self, brand, model, platenum, dayrent, carid, insurance):
        super().__init__(brand, model, platenum, dayrent, carid)
        self.insurance =insurance
    def get_insurance(self):
        return self.insurance
    def calc_rent(self, days, discount=1):#discount折扣
        return super().calc_rent(days, discount=1) + self.insurance * days
class SportCar(Automobile):
    def __init__(self, brand, model, platenum, dayrent, carid, damage):
        super().__init__(brand, model, platenum, dayrent, carid)
        self.damage = damage

    def get_damage(self):
        return self.damage

    # 跑车需要增加损耗费用
    def calc_rent(self, days, discount=1):
        return super().calc_rent(days, discount) + self.damage * days
class SUV(Automobile):
    def __init__(self, brand, model, platenum, dayrent, carid):
        super().__init__(brand, model, platenum, dayrent, carid)
    def calc_rent(self, days, discount=1):
        if days > 7 :
            return super().calc_rent(discount * 0.7)
class CarOperation():
    def __init__(self):
        self.cars = {}
        self.stocks = {'Economy':[], 'Luxury':[], "Sport":[], "SUV":[]}
        self.carid1 = 10000     # 经济车型起始ID
        self.carid2 = 20000     # 豪华车起始ID
        self.carid3 = 30000     # 跑车起始ID
        self.carid4 = 40000     # SUV起始ID
        #开始建设指令
    def operate(self):#整个操作系统分为不同指令函数
        print("欢迎使用鱼C汽车租赁程序")
        while True:
            ins = input("\n1.录入汽车;2.租车服务;3.还车服务;4.退出程序：")
            if ins == '1':
                self.register()
            if ins == '2':
                self.rent_car()
            if ins == '3':
                self.return_car()
            if ins == '4':
                break
        # 录入汽车
    def register(self):
        types = input("\n1.经济车型;2.豪华车;3.跑车;4.SUV：")
        nums = int(input("\n请输入需要录入的数量："))
        for each in range(nums):
            print(f"\n请录入第{each+1}辆车")
            brand = input("品牌：")
            model = input("型号：")
            platenum = input("车牌：")
            dayrent = float(input("租金："))
            if types == "1":
                subsidy = float(input("补贴："))
                economy = EconomyCar(brand, model, platenum, dayrent, self.carid1, subsidy)
                self.stocks['Economy'].append(economy)
                self.cars[self.carid1] = economy
                self.carid1 += 1
            if types == "2":
                insurance = float(input("保险："))
                luxury = LuxuryCar(brand, model, platenum, dayrent, self.carid2, insurance)
                self.stocks['Luxury'].append(luxury)
                self.cars[self.carid2] = luxury
                self.carid2 += 1
            if types == "3":
                damage = float(input("损耗："))
                sport = SportCar(brand, model, platenum, dayrent, self.carid3, damage)
                self.stocks['Sport'].append(sport)
                self.cars[self.carid3] = sport
                self.carid3 += 1
            if types == "4":
                suv = SUV(brand, model, platenum, dayrent, self.carid4)
                self.stocks['SUV'].append(suv)
                self.cars[self.carid4] = suv
                self.carid4 += 1
    #通过get函数得到想要的属性
    def get_stock(self):
        print(f"\n1. 经济车型（享有补贴），共有 {len(self.stocks['Economy'])} 辆。")
        if self.stocks['Economy']:#如果dict的key对应的value是空，则为Flase
            for each in self.stocks['Economy']:
                print(f"车辆编号：{each.get_carid()}，品牌：{each.get_brand()}，型号：{each.get_model()}，日租金：{each.get_dayrent()} - {each.get_subsidy()}(补贴)元")

        print(f"\n2. 豪华车（需额外购买保险），共有 {len(self.stocks['Luxury'])} 辆。")
        if self.stocks['Luxury']:
            for each in self.stocks['Luxury']:
                print(f"车辆编号：{each.get_carid()}，品牌：{each.get_brand()}，型号：{each.get_model()}，日租金：{each.get_dayrent()} + {each.get_insurance()}(保险)元")

        print(f"\n3. 跑车（需增加损耗费用），共有 {len(self.stocks['Sport'])} 辆。")
        if self.stocks['Sport']:
            for each in self.stocks['Sport']:
                print(f"车辆编号：{each.get_carid()}，品牌：{each.get_brand()}，型号：{each.get_model()}，日租金：{each.get_dayrent()} + {each.get_damage()}(损耗)元")

        print(f"\n4. SUV（租赁超过7天，享有额外折上7折优惠），共有 {len(self.stocks['SUV'])} 辆。")
        if self.stocks['SUV']:
            for each in self.stocks['SUV']:
                print(f"车辆编号：{each.get_carid()}，品牌：{each.get_brand()}，型号：{each.get_model()}，日租金：{each.get_dayrent()}元")
    # 租车服务
    def rent_car(self):
        self.get_stock()
        
        carid = int(input("\n请输入需要租赁的车辆编号："))
        if self.cars.get(carid):
            car = self.cars[carid]
            if carid // 10000 == 1:
                self.stocks['Economy'].remove(car)
            if carid // 10000 == 2:
                self.stocks['Luxury'].remove(car)
            if carid // 10000 == 3:
                self.stocks['Sport'].remove(car)
            if carid // 10000 == 4:
                self.stocks['SUV'].remove(car)

            days = int(input("请输入需要租赁的天数："))
            # 租赁超过3天，享有9折优惠
            if days > 5:
                cost = car.calc_rent(days, discount=0.8)
            elif days > 3:
                cost = car.calc_rent(days, discount=0.9)
            else:
                cost = car.calc_rent(days)

            print(f"租赁{days}天，总共需要花费：{cost:.2f}元")
            print("恭喜，租赁成功~")

    # 还车服务
    def return_car(self):
        carid = int(input("请输入车辆编号："))
        if self.cars.get(carid):
            car = self.cars[carid]
            if carid // 10000 == 1:
                self.stocks['Economy'].append(car)
            if carid // 10000 == 2:
                self.stocks['Luxury'].append(car)
            if carid // 10000 == 3:
                self.stocks['Sport'].append(car)
            if carid // 10000 == 4:
                self.stocks['SUV'].append(car)
            print("恭喜，还车成功~")
main = CarOperation()
main.operate()