import sys

f = open('input.txt', 'r')

arr = [[0 for x in range(1000)] for x in range(1000)]

for line in f:
   a = line.split()
   if a[0] == "turn":
      x = int(a[2].split(',')[0])
      y = int(a[2].split(',')[1])
      j = int(a[4].split(',')[0])
      k = int(a[4].split(',')[1])
      
      if a[1] == "on":
         val = 1
      else:
         val = 0
      for h in range(x, j+1):
         for i in range(y, k+1):
            arr[h][i] = val

   elif a[0] == "toggle":
      x = int(a[1].split(',')[0])
      y = int(a[1].split(',')[1])
      j = int(a[3].split(',')[0])
      k = int(a[3].split(',')[1])
      
      for h in range(x, j+1):
         for i in range(y, k+1):
            arr[h][i] = (arr[h][i] - 1) * -1

lights = 0
for h in range(1000):
   for i in range(1000):
      lights += arr[h][i]

print lights
