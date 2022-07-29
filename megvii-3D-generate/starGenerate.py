'''
input : ICCV2019-LearningToPaint
output :![Github stars](https://img.shields.io/github/stars/megvii-research/ECCV2022-RIFE?label=ECCV2022-RIFE&color=red)
'''
import os

res = []

left = '![Github stars]('

front = 'https://img.shields.io/github/stars/megvii-research/'
mid = '?label='
back = '&color=red'

right = ')'
with open('./nameList.txt', 'r') as f:
     lines = f.readlines()
     for line in lines:
        line = line.strip()
        if len(line)==0:break
        s = left+front+line+mid+'star'+back+right
        print(s)
        res.append(s)
print(len(res))
with open('./star.txt', 'w') as f:
    for line in res:
        f.write(line+'\n')
