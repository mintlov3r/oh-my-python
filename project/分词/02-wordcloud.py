import wordcloud

import matplotlib.pyplot as plt
import jieba

demo_s = """
我是中国人，我爱自己的国家。
五十六个民族五十六朵花
朵朵哟哪个开在也阳光下
　　党把雨露洒下来哎
　　万紫千红放光华罗
就象是连根的树开出并蒂花
　　开出并蒂花罗哎
　　同为祖国增春光罗哎
　　装点江山美如画罗哎
　　哎罗哩哎哎罗哩哎
　　哎罗哩哎哎罗哩哎
　　装点江山美如画罗
　　五十六个民族五十六朵花
　　朵朵哟哪个开在也迎朝霞
　　党把幸福来播种哎
　　各族人民亲如一家罗
　　就象是长青树岁岁发青芽
　　岁岁发青芽罗哎
"""
# c = jieba.cut(demo_s)
# handle_s = '/'.join([x for x in c if x != ' '])
# print(handle_s)

wc = wordcloud.WordCloud(font_path='./msyh.ttf', background_color='white')

with open('./桃花心木2.txt', encoding='utf-8')as f:
    f_content = f.read()

f_content = jieba.cut(f_content)

wc.generate('/'.join(f_content))

plt.imshow(wc)



wc.to_file('123.png')


