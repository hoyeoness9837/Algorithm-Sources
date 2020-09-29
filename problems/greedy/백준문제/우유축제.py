# 0 1 2 0 1 2 순서로만 가능, 최대 우유 먹을수있는 숫자.
n = int(input())
milk = list(map(int, input().split()))
count = 0

for i in range(n):
    if(milk[i] == count%3):
        count += 1

print(count)
