# print('-'*10)
# print('nihao')
# print('-'*10)

# print('修改end之后')

# print('-'*10, end=' ')
# print('nihao', end=' ')
# print('-'*10, end=' ')
# lst = list(range(10))
# print(lst)
# s = ''.join(list(range(10)))
# print(s)
s = ''.join([str(x) for x in range(10)])
print(s)
print(s[1:4])
print(s[5])
print(s[-2])
print(s[-2:])
print('n'[-2:])
# 逆置所有
print(s[::-1])
print(s[::-1][-2:])