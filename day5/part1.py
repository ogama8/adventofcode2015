import sys

doubles = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']
bad     = ['ab', 'cd', 'pq', 'xy']

f = open('input.txt', 'r')

nice = 0

for line in f:
   vowels = 0
   double = 0
   good   = 1

   for c in line:
      for v in "aeiou":
         if c == v:
            vowels += 1
   
   for d in doubles:
      if d in line:
         double = 1

   for b in bad:
      if b in line:
         good = 0

   if vowels >= 3:
      vowels = 1
   else:
      vowels = 0

   nice += vowels * double * good

print nice

