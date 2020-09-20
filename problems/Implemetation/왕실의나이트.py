## Question ##

# 8*8 체스판에서 나이트(ㄱ만이동가능)말이 첫 시작점이 주어졌을때, 이동가능한 방식의 수를 찾는 알고리즘.
# INPUT = a1
# ANSWER =  2


## My Answer
hor, ver = str(input())
count = 0
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, 2, -2, 1, -1]

def string_to_int(hor):
  if hor =='a':
   return 1
  elif hor =='b':
    return 2
  elif hor =='c':
    return 3
  elif hor =='d':
    return 4
  elif hor =='e':
    return 5
  elif hor =='f':
    return 6
  elif hor =='g':
    return 7
  elif hor =='h':
    return 8

for i in range(8):
  nx = string_to_int(hor) + dx[i]
  ny = int(ver) + dy[i]
  if ny < 1 or ny < 1 or nx > 8 or ny > 8:
    continue
  else:
    count +=1

print(count)

## Solution 1
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1  # a라면, 65-65 +1 = 1이되므로 기준점이되는 a를 빼주는것이 맞다.

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)] #움직일수있는 모든경우의수

result = 0
for step in steps: #steps가 리스트므로, 이미 범위가 8번으로 정해져있음.
  new_row = row + step[0]
  new_col = col + step[1]
  if new_row >=1 and new_col >=1 and new_row<=8 and new_col <=8: #범위내에 참인 모든 패턴을 찾는거이므로 and를 이용. 이전문제에서처럼 범위밖을 벗어나는것을 무시해야하는게 아니므로.
    result +=1

print(result)


## Notes ##
# 1. ord("a")는 ASCII 코드의 숫자를 string으로 리턴한다
# 2. important to know when to use and versus or.
