# 세계적인 도둑 상덕이는 보석점을 털기로 결심했다.
# 상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.
# 상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)
# 다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)
# 다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)
# 첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력한다.
# example) 3 2 | 1 65 | 5 23 | 2 99 | 10 | 2 --> 164

#my answer# timeout.
N, K = map(int, input().split())

gem = []
for i in range(N):
  gem.append(list(map(int, input().split())))

gem = sorted(gem, key = lambda x: x[1], reverse = True)

limit = []
for i in range(K):
  limit.append(list(map(int, input().split())))

count = 0
value = 0
for i in range(N):
  for bag in limit:
    if count == K:
      break
    elif gem[i] > bag:
      continue
    else:
      value += gem[i][1]
      count += 1

print(value)


###ANSWER###
import heapq
import sys
input = lambda: sys.stdin.readline().strip()

N, K = map(int, input().split())

gem = []
for i in range(N):
    M, V = list(map(int, input().split()))
    heapq.heappush(gem, [M, V])

bags = [int(input()) for i in range(K)]
bags.sort()

value = 0
p = []

for i in range(K):
    capacity = bags[i]

    while gem and capacity >= gem[0][0]:
        [M, V] = heapq.heappop(gem)
        heapq.heappush(p, -V)

    if p:
        value -= heapq.heappop(p)
    elif not gem:
        break

print(value)
