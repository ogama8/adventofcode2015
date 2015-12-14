import sys
from pprint import pprint

f = open('input.txt', 'r')

str = f.read()
num_moves = len(str)

arr = [[0 for x in range(num_moves*2 + 1)] for x in range(num_moves*2 + 1)] 

cursor = [num_moves, num_moves]
arr[num_moves][num_moves] = 1
houses = 1

for c in str:
   if c in ['<', '>', '^', 'v']:
      if   c == '<':
         cursor[0] -= 1
      elif c == '>':
         cursor[0] += 1
      elif c == '^':
         cursor[1] -= 1
      elif c == 'v':
         cursor[1] += 1
      
      arr[cursor[1]][cursor[0]] += 1;
      if arr[cursor[1]][cursor[0]] == 1:
         houses +=1


print houses

