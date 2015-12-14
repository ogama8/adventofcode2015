import sys

f = open('input.txt', 'r')
str = f.readline()

floor = 0
count = 0
first = 0
for c in str:
   count += 1
   if c == '(':
      floor += 1
   if c == ')':
      floor -= 1
   
   if floor < 0 and first == 0:
      first = 1
      print count

