import sys

f = open('input.txt', 'r')

paper = 0

for line in f:
   a = [int(x) for x in line.split('x')]
   s1 = a[0]*a[1]
   s2 = a[1]*a[2]
   s3 = a[0]*a[2]

   if   s1 <= s2 and s1 <= s3:
      paper += s1
   elif s2 <= s1 and s2 <= s3:
      paper += s2
   elif s3 <= s1 and s3 <= s2:
      paper += s3

   paper += 2*s1 + 2*s2 + 2*s3

print paper




