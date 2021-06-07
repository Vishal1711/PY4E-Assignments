hrs = input('Enter Hours:')
h = float(hrs)
rate = input('Hours Rate:')
r = float(rate)
if h>40:
    Pay = (40*r)+(h-40)*r*1.5
elif h<0:
    Pay = "Invalid"
    print(Pay)

else:
    Pay = r*h

print(Pay)
