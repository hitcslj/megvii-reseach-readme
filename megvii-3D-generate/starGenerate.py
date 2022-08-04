'''
input : ECCV2022-RIFE
output :<a href="https://github.com/megvii-research/ECCV2022-RIFE"><img src="https://img.shields.io/github/stars/megvii-research/ECCV2022-RIFE?label=star&color=red" /></a>
'''
import os

res = []

left = '<a href="https://github.com/MegviiRobot/'

mid = '"><img src="https://img.shields.io/github/stars/MegviiRobot/'

right = '?style=social" /></a>'


with open('./nameList.txt', 'r') as f:
     lines = f.readlines()
     for name in lines:
        name = name.strip()
        if len(name)==0:break
        s = left+name+mid+name+right
        print(s)
        res.append(s)
print(len(res))
with open('./star.txt', 'w') as f:
    for line in res:
        f.write(line+'\n')
