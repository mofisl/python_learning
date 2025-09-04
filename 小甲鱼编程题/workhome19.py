import time
import hashlib
#Member类是会员代表人
#Mange类是管理
#二者没有继承性，Maxin是操作管理中的密码
#像Member这种把信息储存，考虑将实例对象存为list或者dict,方便操作
class Member:
    def __init__(self, cardid, name, passwd, scores, regdate):
        self.cardid = cardid
        self.name = name
        self.passwd = passwd
        self.scores = scores
        self.regdate = regdate
class PasswdMixin: #没有绑定passwd，
    #密码长度检测
    def is_tooshort(self, passwd, require=6):
        while len(passwd) < require:
            passwd = input("会员密码不能小于6位，请重新输入：")
        return passwd
    #转md5
    def to_md5(self, passwd):
        bstr = bytes(passwd, "utf-8")
        #MD5 加密需要字节类型（bytes）的数据，因此用 bytes() 函数将字符串按 utf-8 编码转换为字节流
        passwd = hashlib.md5(bstr).hexdigest()
        #hashlib.md5(bstr)：创建 MD5 哈希对象并传入字节数据
        #.hexdigest()：将哈希结果转换为 32 位的十六进制字符串
        return passwd
class LoggerMixin:
    def log(self, message, filename = "log.txt"):
        with open(filename,'w') as f:
            f.write(message)
class Manage(PasswdMixin, LoggerMixin):
    def __init__(self):
        self.members = {}
        self.cardid = 10000
    # 程序功能入口
    def welcome(self):
        print("欢迎使用鱼C超市会员管理系统")
        while True:
            ins = input("\n1.创建新卡;2.修改密码;3.商品支付;4.积分查询;5.退出程序：")
            if ins == '1':
                self.create_member()
            if ins == '2':
                self.modify_passwd()
            if ins == '3':
                self.pay_money()
            if ins == '4':
                self.view_scores()
            if ins == '5':
                print("感谢使用鱼C超市会员管理系统")
                break 
    def confirm_passwd(self):
        cardid = int(input('请输入卡号：'))
        while not self.members.get(cardid):
            cardid = int(input("该卡号不存在，请重新输入："))
        passwd = input("请输入密码：")
        passwd = self.to_md5(passwd)
        while not self.members.get(cardid).passwd:
            passwd = input("密码不正确，请输入密码：")
            passwd = self.to_md5(passwd)
        return cardid
    def create_member(self):
        name = input("请输入名字：")
        passwd = input("请输入密码：")
        passwd = self.is_tooshort(passwd)
        passwd = self.to_md5(passwd)
        scores = 0
        regdate = time.localtime()
        member = Member(self.cardid, name, passwd, scores, regdate)
        self.members[self.cardid] = member
        print(f"创建成功，卡号为 {self.cardid}，关联用户 -> {name}")
        self.log(f"开卡成功：{self.cardid} -> {name}，时间：{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        self.cardid += 1
    def modify_passwd(self):
        #修改密码的前提是验证卡号
        cardid = self.confirm_passwd()
        newpasswd = input("请输入新密码：")
        newpasswd = self.is_tooshort(newpasswd)
        newpasswd = self.to_md5(newpasswd)
        self.members[cardid].passwd = newpasswd
        self.log(f"修改密码：卡号 -> {self.cardid}，时间：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n")
    def pay_money(self):
        cardid = self.confirm_passwd()
        money = int(input("请输入支付金额："))
        self.members[cardid].scores += money
        self.log(f"积分累计：卡号 -> {self.cardid}，+{money}分，时间：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n")
    def view_scores(self):
        cardid = self.confirm_passwd()
        print(f"卡号 {cardid} 当前的消费积分为：{self.members[cardid].scores}")


def main():
    m = Manage()
    m.welcome()
main()