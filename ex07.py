fname = input('File Name:')
fhand = open(fname)
count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        number = float(line[20:])
        total = total + number
        continue

print(total)
print(count)
print('Average spam confidence:',(total/count))
