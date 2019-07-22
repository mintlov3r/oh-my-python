from bs4 import BeautifulSoup
import requests


url = 'http://xiaohua.zol.com.cn/detail13/12975.html'
resp = requests.get(url)
# print(resp.text)
soup = BeautifulSoup(resp.text, 'lxml')
# print(soup.prettify())
# print(soup.div)
# print(soup.get_text())
# print(soup.div.string)
for i in soup.find_all("div", class_="article-text"):
    print(i.string)