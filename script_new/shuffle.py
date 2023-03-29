def read(file_name):
    res = []
    with open(file_name, 'r') as f:
         lines = f.readlines()[2:] # skip the first two lines
         for line in lines:
            line = line.strip()
            if len(line)==0:break
            res.append(line)
    return res
res = []
file_names = ['megvii-research','megvii-model','Megvii-BaseDetection','MegEngine','MegviiRobot']
file_names = [f'{file_name}.md' for file_name in file_names]
for file_name in file_names:
    res += read(file_name)
res.sort()
res = ['| name | description |','|-------|-----------|'] + res
file_name = 'all.md'
with open(file_name, "w", encoding="utf-8") as f:
    for line in res:
        f.write(line+'\n')
print(f"Markdown内容已保存到 {file_name}")