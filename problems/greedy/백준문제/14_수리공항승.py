# 항승이는 품질이 심각하게 나쁜 수도 파이프 회사의 수리공이다. 항승이는 세준 지하철 공사에서 물이 샌다는 소식을 듣고 수리를 하러 갔다.
# 파이프에서 물이 새는 곳은 신기하게도 가장 왼쪽에서 정수만큼 떨어진 거리만 물이 샌다.
# 항승이는 길이가 L인 테이프를 무한개 가지고 있다.
# 항승이는 테이프를 이용해서 물을 막으려고 한다. 항승이는 항상 물을 막을 때, 적어도 그 위치의 좌우 0.5만큼 간격을 줘야 물이 다시는 안 샌다고 생각한다.
# 물이 새는 곳의 위치와, 항승이가 가지고 있는 테이프의 길이 L이 주어졌을 때, 항승이가 필요한 테이프의 최소 개수를 구하는 프로그램을 작성하시오. 테이프를 자를 수 없고, 테이프를 겹쳐서 붙이는 것도 가능하다.
# 첫째 줄에 물이 새는 곳의 개수 N과 테이프의 길이 L이 주어진다. 둘째 줄에는 물이 새는 곳의 위치가 주어진다. N과 L은 1,000보다 작거나 같은 자연수이고, 물이 새는 곳의 위치는 1,000보다 작거나 같은 자연수이다.
# example) 4 2 | 1 2 100 101  --> 2

# 내시도
N, L = map(int, input().split())
holes = list(map(int, input().split()))
holes.sort()
count = 0
for i in range(0,N,2):
  if i+1 < N:
    if holes[i] - holes[i+1] <= L-1:
      count+=1
print(count)

 
# 정답
N, L = map(int, input().split())
holes = list(map(int, input().split()))
holes.sort()
count = 1
start = holes[0] #첫 구멍
end = holes[0] + L #첫 구멍에 테이프길이를 더한 값
for i in range(N):
  if start <= holes[i] < end: # 이사이에 위치하면 한 테이프로 막을수있음 시작점이 곂치지않게 마지막 부분은 포함하지 않도록한다.
    continue #그러므로 테이프 갯수를 늘리지 않고 무시
  else:  # 그외에 구멍들 새롭게 테스트.
    start = holes[i]
    end = holes[i] + L
    count += 1
print(count)