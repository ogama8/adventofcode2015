import sys

f = open('input.txt', 'r')
str = f.readline()

floor = 0
for c in str:
   if c == '(':
      floor += 1
   if c == ')':
      floor -= 1

print floor
