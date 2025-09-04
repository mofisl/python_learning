from pathlib import Path
from time import strftime, localtime
def get_file_msg(path):
    p = Path(path)
    paths = []
    files = []
    # 利用glob()函数找出指定路径下的所有文件
    for each in p.glob("**/*"):
        paths.append(each)
        if each.is_file():
            name = each.name
            size = each.stat().st_size
            folder = each.parent.resolve()
            ctime = each.stat().st_ctime
            mtime = each.stat().st_mtime
            atime = each.stat().st_atime
            files.append(File(name, size, folder, ctime, mtime, atime))

    print("路径结构如下：")
    for each in paths:
        print(each)

    return files


def match_file(files):
    count = 0
    filename = input("\n请输入想要搜索的文件名：")
    for each in files:
        if filename in each.name:
            count += 1
            print(f"\n找到相关文件（{count}）-> {each.get_name()}（{each.get_size()}）")
            print(each.get_folder())
            print(each.get_ctime())
            print(each.get_mtime())
            print(each.get_atime())
    else:
        print("找不到相关文件！")
            

files = get_file_msg("D:/py/小甲鱼第二版最新版/课后作业/target")
match_file(files)