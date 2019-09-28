
def routin_func():
    d2 = {'大学': 1}
    print(d2)

    empty_dict = {'大学': 0,
                '学院': 0}
    if '大学' in line:
        d2['大学'] += 1


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

if __name__ == '__main__':
    keyword_list = ['大学', '学院']
    str_list = ['大学真好啊', '你是谁呀', '学院' , '大学' '学院啊', 'jog大学ewjog', '大学是什么？']
    d = gen_dict(keyword_list, str_list)
    print(d)
