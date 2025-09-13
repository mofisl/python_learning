from hello import * #这种是直接导入
say(x)
x= 30
say(x)
# ok(y)
# #NameError: name 'ok' is not defined

import hello as helloa #这种必须加前缀
helloa.ok(helloa.y)#
