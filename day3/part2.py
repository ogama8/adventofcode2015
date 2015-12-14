import sys
from pprint import pprint

f = open('input.txt', 'r')

str = f.read()
num_moves = len(str)

arr = [[0 for x in range(num_moves*2 + 1)] for x in range(num_moves*2 + 1)] 

cursor  = [[num_moves, num_moves],
           [num_moves, num_moves]]

arr[num_moves][num_moves] = 2
houses = 1
cur_sel = 0;

for c in str:
   if c in ['<', '>', '^', 'v']:
      cur_sel += 1
      cur_sel = cur_sel % 2
      
      if   c == '<':
         cursor[cur_sel][0] -= 1
      elif c == '>':
         cursor[cur_sel][0] += 1
      elif c == '^':
         cursor[cur_sel][1] -= 1
      elif c == 'v':
         cursor[cur_sel][1] += 1
      
      arr[cursor[cur_sel][1]][cursor[cur_sel][0]] += 1;
      if arr[cursor[cur_sel][1]][cursor[cur_sel][0]] == 1:
         houses +=1


print houses

