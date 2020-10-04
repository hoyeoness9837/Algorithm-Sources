# 무게가 양의 정수인 N개의 저울추가 주어질 때, 이 추들을 사용하여 측정할 수 없는 양의 정수 무게 중 최솟값을 구하는 프로그램을 작성하시오.
# 예를 들어, 무게가 각각 3, 1, 6, 2, 7, 30, 1인 7개의 저울추가 주어졌을 때, 이 추들로 측정할 수 없는 양의 정수 무게 중 최솟값은 21이다. 
n = int(input())
data = list(map(int, input().split()))
data = sorted(data, reverse=True)
result = 1
for i in range(1,n):
  if data[0] > data[i]:
    result += data[i]
print(result)

##정답##
n = int(input())
data = list(map(int, input().split()))
data.sort()
result = 1
for i in range(n): # 1 + (1 + 1 + 2 + 3 + 6 + 7) = 21, 2<1 -> 3<2 -> 5< 3 -> 11< 6 -> 21 < 30
    if result < data[i]: # 1에다가 i번째까지 더한 값이 최솟값라고할때, 그다음큰 한개의 추보다 합이 작아지기 전까지 더해주다 멈춘다. 왜나면, 그 추 하나만 더해도 최솟값을 넘기므로. 더이상 최솟값이아님.
        break
    result += data[i]
print(result)