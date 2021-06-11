import re
fname = input('Enter File Name:')

fhand = open(fname)
lst = list()
count = 0
for line in fhand:
    line = line.rstrip()
    x = re.findall('[0-9]+',line)
    for val in x:
        val = float(val)
        lst = lst + [val]
        count = count + 1

Total = sum(lst)
Total = int(Total)
print(Total,count)
