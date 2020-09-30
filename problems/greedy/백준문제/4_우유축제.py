# 0 1 2 0 1 2 순서로만 가능, 최대 우유 먹을수있는 숫자.  0 이 나오지 않으면 아예먹지못함.
n = int(input())
milk = list(map(int, input().split()))
count = 0

for i in range(n):
    if(milk[i] == count%3):
        count += 1

print(count)
