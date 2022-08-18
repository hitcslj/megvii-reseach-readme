

def read(file_name):
    res = []
    with open(file_name, 'r') as f:
         lines = f.readlines()
         for line in lines:
            line = line.strip()
            if len(line)==0:break
            res.append(line)
    return res
res = []
file_names = ['megvii-research-generate/table.txt','megvii-basemodel-generate/table.txt','megvii-BaseDetection/table.txt','megvii-3D-generate/table.txt','megvii-MegEngine/table.txt']
for file_name in file_names:
    res += read(file_name)
res.sort()
with open('./table.txt', 'w') as f:
    for line in res:
        f.write(line+'\n')