import string
fname = input('Enter File Name:')
fhandle = open(fname)

di = dict()

for line in fhandle:
    if line.startswith('From '):
        line = line.rstrip()
        line = line.split()
        email = line[5]
        a = email.split(':')
        time = a[0]
        di[time] = di.get(time,0) + 1



lst = list()
for k,v in list(di.items()):
    lst.append((k,v))

lst.sort()

for k,v in lst:
    print(k,v)
