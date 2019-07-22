import requests
from lxml import etree

root_url = 'http://www.chnu.edu.cn/Item/132040.aspx'

response = requests.get(root_url)

html = etree.HTML(response.text)
target = html.xpath('//*[@id="fontzoom"]/p/text()')
file = open('./hbsf_2.txt', 'a+', encoding='utf-8')
for item in target:
    # print(item)
    file.write(item.strip()+'\n'+'\n')
# file.write('\n'.join([x.strip() for x in target]))
file.close()
print('爬取成功！')