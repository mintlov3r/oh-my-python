# Day 2
## 第二天任务
python语法精进

## 爬虫回顾



```python
# 爬虫精进
import requests
url = ''
resp = requests.get(url)


```

## 列表生成式

```python
a = [str(x) for x in list(range(100))]
b = ', '
c = b.join(a)
# 假如我们爬虫爬到一个列表，可以采用下面的方法直接写入文件
d = '\n'.join(a)
with open('wenjianming.txt', 'w') as f:
    f.write(d)
```

## 接下来需要掌握的

```python
# zip  打包
# namedtuple  具名元组 
# list $ 列表
# tuple $ 元组
# set  集合
# dict $  字典
# queue  队列

```



## 每日一练

### q1. 编写脚本，输出提示，按提示输入一个名字，并打印出来

需要达到如下效果

请输入一个名字：

aaa

你输入的名字是：

aaa


```python
a = input('请输入一个名字:\n')

print('你输入的名字是：\n{}'.format(a))
```



### 格式化输出

```python

a = '1'

b = '2'

c = '-{}&&&{}-'.format(a, b)

print(c)

print('-'*23)


```

