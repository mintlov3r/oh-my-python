import re
l = [
    '12132f2',
    '45254252',
    '12345678901',
    'qrqrqw12143',
    '11111111111',
    '12345678921',
    '12345228901',
    's11234111190s',
    '1234',
    '12345671',

]
# 定义，纯数字，且11位号码即为电话号码
# \d decimal
l_new = []
for s in l:
    # rs = re.search('^[\d]{11}$', s)
    rs = re.search('[\d]{11}', s)
    if rs:
        print(rs.group())
        l_new.append(rs.group())
    
print(l_new)

