import jieba


s = '我是小明，我爱中国，我很好'


cut = jieba.cut(s)

# print(cut)

# for t in cut:
#     print(t, end='|')
# 我|是|小明|，|我|爱|中国|，|我|很|好|

# d = {'我':3, '中国':2}

d_tmp = {}
for t in cut:
    if t not in d_tmp:
        d_tmp[t] = 1
    else:
        d_tmp[t] += 1

print(d_tmp)