# 그리디 알고리즘 + BFS문제
# 최대한 많은 가스관을 배치하기 위해선, 가스관이 가급적 우상향이 되어야 하므로, 우상향-직진-우하향 순서대로 파이프를 설치할 수 있는지 확인해야한다.


#solution 1
def solve(i, j):
  if j == C -1: # 끝나는 지점이라면, 
    return True # 참 반환
  
  for d in dx: # 변할수 있는 부분에서 (우상, 직진, 우하 순서로)
    if 0 <= i+d < R and table[i+d][j+1] == '.' and not visit[i+d][j+1]: # 만약 이동한부분이 주어진 맵 안에있고, 비어있는곳이고, 방문한적이없는곳이라면
      visit[i+d][j+1] = True # 해당 파아프 방문처리.
      if solve(i+d, j+1): #방문처리가 되어있다면, 
        return True # 참 반환

  return False # 그외에는 거짓반환

R, C = map(int, input().split())
table = [list(input().rstrip()) for _ in range(R)]
visit = [[False] * C for _ in range(R)]
dx = [-1, 0, 1]
answer = 0

for i in range(R):
  if table[i][0] == '.': # 만약 맵이 비어있다면,
    if solve(i, 0): # 만약 참반환곳(도착지점이 방문처리가 되었다면)
      answer += 1 # 결과값 1씩 증가.
print(answer)



#solution 2
import sys
r, c = map(int, sys.stdin.readline().split())
maps = []
for y in range(r):
  arr = list(sys.stdin.readline().replace("\n", ""))
  maps.append(arr)

directions = [(-1,1), (0,1),(1,1)]
end_line = len(maps[0])-1

def connect_pipe(y: int, x:int) ->(bool):
  maps[y][x] = 'x'
  if x == end_line:
    return True
  
  for dy, dx in directions:
    ny, nx = y+dy, x+dx

    if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] == '.':
      if connect_pipe(ny, nx):
        return True
  
  return False

answer = 0
for y in range(len(maps)):
  if connect_pipe(y,0):
    answer += 1

print(answer)