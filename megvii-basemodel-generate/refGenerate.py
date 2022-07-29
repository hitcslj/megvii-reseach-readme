'''
input : ShuffleNet-Series
output : [ShuffleNet-Series](https://github.com/megvii-model/ShuffleNet-Series)
'''

import os


res = []
front = 'https://github.com/megvii-model/'

with open('./nameList.txt', 'r') as f:
     lines = f.readlines()
     for line in lines:
        line = line.strip()
        if len(line)==0:break
        s = '['+line+']'+'('+front+line+')'
        print(s)
        res.append(s)
print(len(res))
with open('./ref.txt', 'w') as f:
    for line in res:
        f.write(line+'\n')


