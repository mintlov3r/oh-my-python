import requests
from lxml import etree

root_url = 'http://xiaohua.zol.com.cn/detail13/12975.html'
response = requests.get(root_url)

html = etree.HTML(response.text)
target = html.xpath('//div[@class="article-text"]/text()')
file = open('./xiaohua.txt', 'a+', encoding='utf-8')
for item in target:
    file.write(item.strip()+'\n')

file.close()

# with open('./**.txt', 'a+', encoding='utf-8') as f:
#     f.write('')