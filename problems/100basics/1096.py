# 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
# n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.
n = int(input())
array = [[0] * 19 for _ in range(19)]
for i in range(n):
  a, b = input().split()
  x = int(a)
  y = int(b)
  array[x-1][y-1] = 1

for i in range(19):
  for j in range(19):
    print(array[i][j], end=" ")
  print(end='\n')