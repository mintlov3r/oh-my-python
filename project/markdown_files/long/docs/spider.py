# spider


# coding:utf-8

import requests
from lxml import etree

root_url = 'http://xiaohua.zol.com.cn/lengxiaohua/'

response = requests.get(root_url)
# print(response.text)

# filename = './xiaohua2.txt'
# with open(filename, mode='a+',encoding='utf-8') as fw:
#     fw.write(response.text)
# list

html = etree.HTML(response.text)
target = html.xpath('//div[@class="summary-text"]/p/text()')
file = open('./xiaohua_qx_1.txt', 'a+', encoding='utf-8')
for item in target:
    # print(item.strip())
    file.write(item.strip()+'\n')

file.close()
