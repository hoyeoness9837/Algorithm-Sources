# https://www.acmicpc.net/problem/13305

#myanswer
N = int(input())
distance = list(map(int, input().split()))
gas = list(map(int, input().split()))

cost = 0
first = distance[0] * gas[0]
min_cost = distance[1] * gas[1]
for i in range(2, N - 1):
    if distance[i] * gas[i] < min_cost:
        min_cost = distance[i] * gas[i]
    cost += min_cost
print(cost + first)


#answer 
N = int(input())
d = [0] * N # 결과를 담을 비용을 리스트초기화
distance = list(map(int, input().split()))
distance.append(0) # 한자리 부족한 마지막 인덱스를 채워주기위해.
gas = list(map(int, input().split()))


min_gas = gas[0] #가상의 최솟기름값.
d[0] = distance[0] * gas[0] #맨 처음 도시에서 두번째까지는 꼭 0,0 을이용해야만 가능.
for i in range(1, N): # 위 0,0 부분을 뺀.
  if gas[i] < min_gas: # 만약 이보다 작은기름값이 있다면, 그 기름값을 최솟값으로 바꿈.
    min_gas = gas[i]
  d[i] = d[i-1] + min_gas * distance[i]  # 결과를 담을 비용은 이전비용에다가 최소기름값에 각 거리를 더한값으로 대입.
print(d[N-1]) # 모든 가스값을 체크하여 결과를 담은 마지막 총 비용값을 출력.
