'''
input : ECCV2022-RIFE
output : [ECCV2022-RIFE](https://github.com/megvii-research/ECCV2022-RIFE)
'''

import os


res = []
front = 'https://github.com/megvii-research/'

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


