import sys

f = open('input.txt', 'r')

ribbon = 0

for line in f:
   a = sorted([int(x) for x in line.split('x')])
   
   ribbon += 2*a[0] + 2*a[1]
   ribbon += a[0] * a[1] * a[2]

print ribbon

