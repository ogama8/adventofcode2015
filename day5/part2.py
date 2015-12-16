import sys

f = open('input.txt', 'r')

nice = 0

for line in f:
   repeat = 0
   sando  = 0

   for i in range(len(line) - 3):
      if line[i:i+2] in line[i+2:]:
         repeat = 1
   
   for i in range(len(line) - 2):
      if line[i] == line[i+2]:
         sando = 1

   nice += repeat * sando

print nice

