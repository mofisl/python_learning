from pathlib import Path
from time import ctime, strftime, localtime
class Pathfind:
    def __init__(self, name, size, pos, ctime, mtime, atime):
        self.name = name
        self.size = size
        self.pos = pos
        self.ctime = ctime
        self.mtime = mtime
        self.atime = atime
    def get_name(self):
        return self.name
    def get_size(self):
        return f'文件大小{self.size}'
    def get_pos(self):
        return f'文件位置{self.pos}'
    def get_ctime(self):
        return f"创建时间：{strftime('%Y-%m-%d %H:%M:%S', localtime(self.ctime))}"
    def get_mtime(self):
        return f"修改时间：{strftime('%Y-%m-%d %H:%M:%S', localtime(self.mtime))}"
    def get_atime(self):
        return f"访问时间：{strftime('%Y-%m-%d %H:%M:%S', localtime(self.atime))}"
def get_file_msg(path):
    p = Path(path)
    paths = []
    files = []
    for each in p.glob('**/*'):
        paths.append(each)
        if each.is_file():
            name = each.name
            size = each.stat().st_size
            pos = each.parent.resolve()
            ctime = each.stat().st_birthtime
            mtime = each.stat().st_mtime
            atime = each.stat().st_atime
            files.append(Pathfind(name, size, pos, ctime, mtime, atime))
    print(files)
    for each in paths:
        print(each)
    return files
    
def match_file(files):
    filename = input('请输入文件名:')
    count = 0
    for each in files:
        if filename in each.name:#把属性从对象取出来
            count += 1
            print(f"\n找到相关文件（{count}）-> {each.get_name()}（{each.get_size()}）")
            print(each.get_pos())
            print(each.get_ctime())
            print(each.get_mtime())
            print(each.get_atime())
    else:
        print("找不到相关文件！")
files = get_file_msg(r"D:\py\小甲鱼第二版最新版\课后作业\target")
match_file(files)