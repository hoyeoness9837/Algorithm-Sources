n, m = map(int, input().split())

# 띄어쓰기없이 행렬좌표가 들어올때 입력법
A = [list(map(int, list(input()))) for _ in range(n)] 
B = [list(map(int, list(input()))) for _ in range(n)]

def flip(x,y): # 3*3크기의 부분 행렬에 모든 원소에대해 (0 -> 1, 1 -> 0)
  for i in range (x, x+3):
    for j in range (y, y+3):
      A[i][j] = 1 - A[i][j] # (0 -> 1, 1 -> 0)로 바꿔주는 연산.

def checkEquality(): 
  for i in range(n):
    for j in range(m):
      if A[i][j] != B[i][j]: #행렬 A, B가 다른지 확인하고
        return 0 # 다르다면 False 반환
  return 1 # 다르지 않다면 True 반환 

count = 0
for i in range(0, n-2): #플립해줄 부분행열의 크기가 n*m내에서의  3*3이므로 
  for j in range(0, m-2):
    if A[i][j] !=B[i][j]: #행렬이 같지 않다면, 
      flip(i,j) # 플립(i->i+3, j->j+3)안의 모든 원소를 뒤집어준다.
      count += 1  # 뒤집은 횟수 카운트

if checkEquality():
  print(count) # 플립후 행렬이 같다면, 카운트 반환
else:
  print(-1) # 플립후 행렬이 다르다면, -1 반환