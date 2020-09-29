import heapq #이문제를 위해 힙정렬 사용

def solution(N, logs): 
  heapq.heapify(logs) # 입력된 통나무높이 리스트를 힙으로 트랜스폼
  my_logs = [0] * N  # 새로 정렬될 리스트 초기화
  left = 0  # 가장 왼쪽 인덱스
  right = -1 # 가장 오른쪽 인덱스
  for _ in range(N//2): # 왼쪽 오른쪽 한번에 두개씩 들어가므로 총 길이의 절반만 반복.
    my_logs[left] = heapq.heappop(logs) # 힙리스트중 가장 작은수를 새로정렬될 리스트 왼쪽에 삽입
    my_logs[right] = heapq.heappop(logs) # 그다음에 다른 가장 작은 수를 새로정렬될 리스트 오른쪽에 삽입
    left += 1 # 한칸씩 중앙쪽으로 이동
    right += -1 # 한칸씩 중앙쪽으로 이동 
  if logs: #큐에 통나무가 아직 남아있다면,
    my_logs[left] = heapq.heappop(logs) # 남은것은 왼쪽에 넣어줌

  answer = 0
  for i in range(N):
    answer = max(answer, abs(my_logs[i] - my_logs[i-1]))# 각통나무들 높이 차이중에서 가장 큰 값을 반환. 

  print(answer)


t = int(input())
for i in range(t):
  n = int(input())
  logs = list(map(int, input().split()))
  solution(n, logs)


  #answer = max(answer, abs(my_logs[i] - my_logs[i-1]))에서 i+1을 사용하지 않아야 범위안에서 비교가능.