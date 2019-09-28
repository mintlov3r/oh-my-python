# coding:utf-8
import random
import string
RANDOM_STRING = ['学院', '大学', '中国', '世界', '好的']

def read_from_file(filename):
    """从文件读取数据，并返回列表格式的数据"""
    with open(filename, encoding='utf-8') as f:
        frl = f.readlines()
    return [x.strip() for x in frl]

def handle_data(data_list):
    handle_list = [x for x in data_list if ('大学' in x) or ('学院' in x)]
    return handle_list

def gen_dict(keyword_list, lines):
    d3 = {}
    for line in lines:
        for keyword in keyword_list:
            if keyword in line:
                if keyword in d3:
                    d3[keyword] += 1
                else:
                    d3[keyword] = 1
    return d3

def write_to_file(filename, handle_list):
    with open(filename, mode='w', encoding='utf-8') as f:
        for i in handle_list:
            f.write(i+'\n')
    print('success!\n')


def add_to_file(filename, d):
    with open(filename, mode='a', encoding='utf-8') as f:
        f.write('\n')
        f.write(str(d)+'\n')
    print('success!\n')

def solution_1():
    list_1 = read_from_file('./fake.txt')
    list2 = handle_data(list_1)
    write_to_file('solution.txt', list2)


def solution_2():
    list_1 = read_from_file('./fake.txt')
    d = gen_dict(['大学', '学院'], list_1)
    add_to_file('./fake.txt', d)

def fake_data_to_file(filename):
    with open(filename, mode='w', encoding='utf-8') as f:
        content = '\n'.join([str(random.choice(RANDOM_STRING)+''.join(
            random.sample(string.ascii_letters + string.digits, 20)))
                            for i in range(10)])
        f.write(content)

if __name__ == '__main__':
#     # fake_data_to_file('fake.txt')
#     lst = read_from_file('./fake.txt')
#     lst2 = handle_data(lst)
#     write_to_file(lst2)
    solution_2()
    