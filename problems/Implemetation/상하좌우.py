## Question ##

# In between N*N map, starting from 1,1 move L=left, R=right, U=upward, d=downward. calculate where you is your destiniation is located at. ignore anymoves if the move exceeded outside of the map.
# INPUT = 5 | R R R U D D
# ANSWER =  3 4


## My Answer
n = int(input())
a=1
b=1
plan = list(map(str,input().split()))

for i in range(len(plan)):
  while n > 0:
    if(plan[i] == 'R'):
      a +=1
    elif(plan[i] == 'D'):
      b +=1
    elif(plan[i] == 'L'):
      a -=1
    elif(plan[i] == 'U'):
      b -=1
    n-=1
  i+=1

print(a,b)
#result = 6 1

## Solution 1
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ['L', 'R', 'U', 'D']

for plan in plans: # check every plan in plans
  for i in range(len(move_types)): #compare and if they match, move
    if move_types[i]==plan:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx < 1 or ny < 1 or nx > n or ny > n: #if it moves out of range, ignore
    continue
  x, y = nx, ny

print(x,y)

## Notes ##
#1. how to set the movement in list is important
#2. how and when to use for/while
#3. if & continue to for ignoring some conditions, (difference btw break, pass ... )