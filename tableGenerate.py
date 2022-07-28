'''
input : name | description | star
output :| [ECCV2022-RIFE](https://github.com/megvii-research/ECCV2022-RIFE)  | ECCV2022-Real-Time Intermediate Flow Estimation for Video Frame Interpolation. | ![Github stars](https://img.shields.io/github/stars/megvii-research/ECCV2022-RIFE?label=ECCV2022-RIFE&color=red)|
'''

import os

res = []

names = []
descriptions = []
stars = []
with open('./ref.txt', 'r') as f:
     lines = f.readlines()
     for line in lines:
        line = line.strip()
        if len(line)==0:break
        names.append(line)

with open('./description.txt', 'r') as f:
     lines = f.readlines()
     for line in lines:
        line = line.strip()
        if len(line)==0:break
        descriptions.append(line)

with open('./star.txt', 'r') as f:
     lines = f.readlines()
     for line in lines:
        line = line.strip()
        if len(line)==0:break
        stars.append(line)

res = []
for name,description,star in zip(names,descriptions,stars):
    s = '| '+name +' | ' + description+' | ' + star + ' |'
    res.append(s)
    print(s)

with open('./table.txt', 'w') as f:
    for line in res:
        f.write(line+'\n')





