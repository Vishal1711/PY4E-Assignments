fname = input('Enter Name of File:')
fhand = open(fname)

di = dict()
for line in fhand:
    if line.startswith('From '):

        line = line.split()
        day = line[1]
        di[day] = di.get(day,0) + 1

largest = -1
mail = None
for k,v in di.items():

    if v > largest:
        largest = v
        mail = k


print(mail,largest)
