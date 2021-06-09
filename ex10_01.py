fname = input('Enter File Name:')
fhand = open(fname)
di = dict()

for line in fhand:
    if line.startswith('From '):
        line = line.rstrip()
        line = line.split()
        words = line[1]
        di[words] = di.get(words,0) + 1



lst = list()
for key,value in list(di.items()):
    lst.append((value,key))

lst.sort(reverse=True)

print(lst[0])
