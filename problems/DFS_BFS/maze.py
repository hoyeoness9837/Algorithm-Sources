## Question ##

# starting from (1,1), the exit is located at (N,M). Monsters are at 0 and clean path is 1. find shortest way to excape the maze. 
# INPUT =  5 6
# 101010
# 111111
# 000001
# 111111
# 111111
# ANSWER = 10


## My Answer


## Solution 1
from collections import deque # 가장 짧은 길을 찾는것이므로

n,m = map(int, input().split()) 

graph = []
for i in range(n):
  graph.append(list(map(int, input()))) # 이부분이 많이 나옴. 외우기

dx = [-1,1,0,0] #  bfs에서 좌 우
dy = [0,0,-1,1] #  후 상

def bfs (x, y):
  queue = deque() # 일단 큐를 사용하기위해 deque로 정의
  queue.append((x, y)) # bfs함수에서 받아온 좌표를 큐에 삽입한다.

  while queue: #큐에 모든 노드가 나올때까지, 즉 비어있을때 까지 반복
    x,y = queue.popleft() # 들어간 노드를 큐에서 꺼내고 
    for i in range(4): # 방문하지않은 인접 노드를 모드 큐에 삽입.
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue # 새로 큐에 넣으려는 큐가 범위를 벋어났거나 출구보다 크거나 같다면 스킵
      
      if graph[nx][ny] == 0: 
        continue # 새로 움직인 자리에 괴물(벽)이있다면 스킵
      
      if graph[nx][ny] == 1: #새로 움직인 자리가 빈 곳이라면,
        graph[nx][ny] = graph[x][y] + 1 #이동하고, 1 이동했으므로 1을 더해준다.
        queue.append((nx,ny)) # 라인30처럼 큐에 넣어 다음 인접노드에 대해 반복처리할수있도록함. 큐가 비면 끝나므로
  
  return graph[n-1][m-1] # 마지막으로 출구에 도착했을때,(1,1 에서 시작했으므로 이를 뺸값) 라인45에서 더해진 1만큼의 수를 반환.
  
print(bfs(0,0))


## Notes ##