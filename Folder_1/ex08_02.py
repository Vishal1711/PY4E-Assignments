fname = input('Enter File Name:')
fhand = open(fname)
count = 0
for line in fhand:
    words = line.rstrip().split()
    if len(words)<3 or words[0]!='From':
        continue
    count = count + 1
    print(words[1])

print('There were', count, 'lines in the file with From as the first word')
