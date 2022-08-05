def read(file_name):
    res = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if len(line)==0:break
            res.append(line)
    return res

filename_list = ['megvii-research-generate/table.txt','megvii-basemodel-generate/table.txt','megvii-3D-generate/table.txt']

res = []
for file_name in filename_list:
    res += read(file_name)
res.sort()

with open('./table.txt', 'w') as f:
    for line in res:
        f.write(line+'\n')
