#DFS by recursive funcion#
def dfs(graph, v, visited): # 재귀함수는 graph:데이터, v:각 노드, visited:끝낼조건
  visited[v] = True # 여기 들어온 노드는 방문했다라고 정함.
  print(v, end=' ')  # ends the output(v) with a <space> 

  for i in graph[v]: # 입력한 그래프의 노드입력.
    if not visited[i]: # 만약 방문한 적이 없는 노드면, 
      dfs(graph, i, visited) # 다시 재귀함수로써 위에 과정을 새로운 노드로 반복.

graph = [
  [], # 0 => 아무것도 없음. 왜 0자체를 넣냐면 리스트는 인덱스가 0부터 시작하므로.
  [2,3,8], # 1번노드와 연결된것 -> 2번, 3번, 8번 노드
  [1,7], # 2번 노드와 연결된것 -> 1번, 7번 노드
  [1,4,5], 
  [3,5], 
  [3,4], 
  [7], 
  [2,6,8], 
  [1,7], 
]

visited = [False] * 9 # 초기화. 지금 모든 0-9번 
dfs(graph, 1, visited) # 탐색할 그래프, 첫 노드의 번호는 1, 방문값=모두false입력.



#BFS by 
from collections import deque # BFS는 queue기반이므로 deque라이브러리를 이용해 구현

def bfs(graph, start, visited): #처음 시작 노드를 받아온다
  queue = deque([start]) # 받아온 첫 노드를 큐에 삽입한다.
  visited[start] = True # 큐에 삽입후, 노드를 방문확인처리한다.
 
  while queue: # 큐가 비어있지않으면, 즉 삽입한 노드들이 아직 다 나오지 않았다면.
    v = queue.popleft() # 큐에 처음으로 들어간 노드를 하나 뺀다.
    print(v, end=' ') # 뺀노드를 순차적으로 프린트한다.
    
    for i in graph[v]: # 그래프의 깊이만큼 반복.
      if not visited[i]: # 만약 방문하지 않아본 노드라면
        queue.append(i) # 이노드를 큐에 삽입한다.
        visited[i] = True # 삽입된 후, 그 큐들을 방문함 처리한다.

graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5], 
  [3,5], 
  [3,4], 
  [7], 
  [2,6,8], 
  [1,7]
]

visited = [False] * 9
bfs(graph, 1, visited)