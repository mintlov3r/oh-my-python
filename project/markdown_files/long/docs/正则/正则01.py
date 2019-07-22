'''
re
给你一组字符串，列表
挑出符合邮箱规范的字符串，并封装成列表返回
邮箱规范
xxx@xxx.com
xxx@xxx.net
xxx@xxx.cn

字符串示例：
oijgwo8jgwoge*lks
jgdso@jog.com
jlsg@00ljdjs.net
9080098009@sks904.com
'''

import re

def identify(s):
    """
    传入一个字符串，如果符合邮箱规范，则返回true，否则返回false
    """
    result = re.search('[\w]+@[\w]+.(com|net|cn)',s)
    if result:
        return True
        print(result.group())
    return False
s = 'jgdsojog.com'
lst = [
    'jgowjegoj@4022.com',
    'qwrewq.com',
    '123@wqe.com',
    'asd@sad.net',
    'asdasd@kjfldsj.cn',
    '@gjeowe.net'
]
new_list = []
for i in lst:
    if identify(i):
        new_list.append(i)
print(new_list)



# *任意字符 linux *.py dsgw.py sdfsgd.py
# xxx.pyxx  *.py*
# \d 数字, \D 非数字, \w 数字字母下划线, \W