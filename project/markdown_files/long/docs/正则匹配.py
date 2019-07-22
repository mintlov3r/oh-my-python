import glob
import os

# glob.glob('*.txt')

for name in glob.glob('正则/*.md'):
    print(name)

print('-'*20)
for i in os.listdir('正则'):
    print(i)
