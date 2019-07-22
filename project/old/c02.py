# # print()
import os
# # input() # scanf

# # a = input('nihao:\n')

# # print('你输入的字符串是：\n{} {}'.format(a, 67))
newname = ''

# a = 56
# b = 39
# print('a+b=', a+b)

folder_name = './aaa'
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

# for i in range(1000):
#     with open('{}/file-{}.txt'.format(folder_name, i), mode='w', encoding='utf-8') as f:
#         f.write('this is the {} file\n'.format(i))


for i in os.listdir(folder_name):
    new_name = i.replace('file', newname)
    # print(i)
    os.rename('{}/{}'.format(folder_name, i), '{}/{}'.format(folder_name, new_name))