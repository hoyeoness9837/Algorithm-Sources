# 병든 나이트가 N × M 크기 체스판의 가장 왼쪽아래 칸에 위치해 있다. 병든 나이트는 건강한 보통 체스의 나이트와 다르게 4가지로만 움직일 수 있다.
# 2칸 위로, 1칸 오른쪽
# 1칸 위로, 2칸 오른쪽
# 1칸 아래로, 2칸 오른쪽
# 2칸 아래로, 1칸 오른쪽
# 병든 나이트는 여행을 시작하려고 하고, 여행을 하면서 방문한 칸의 수를 최대로 하려고 한다. 병든 나이트의 이동 횟수가 4번보다 적지 않다면, 이동 방법을 모두 한 번씩 사용해야 한다. 이동 횟수가 4번보다 적은 경우(방문한 칸이 5개 미만)에는 이동 방법에 대한 제약이 없다.
# 체스판의 크기가 주어졌을 때, 병든 나이트가 여행에서 방문할 수 있는 칸의 최대 개수를 구해보자.

##my answer
n,m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

steps = [(1,2), (2,1), (-1,2),(-2,1)]
row = n
col = 1
result = 1
while result > 4:
  for step in steps:
    row += step[0]
    col += step[1]
    if row<=n and col<=m :
      result +=1
else:
  for step in steps:
    row += step[0]
    col += step[1]
    result +=1

print(result)

####Answer####
#hint: 나이트는 항상 오른쪽으로만 이동가능. 4번 이상 이동시 모든 방법이 한번 이상씩 사용되어야함. 
n,m = map(int, input().split())

result = 1
if n ==1 or m == 1:
  result = 1
elif n == 2: # 세로가 2칸안에서는 위로 아래로 1씩 움직이는 2,3 번만 사용가능, 여기서 2번이상 이동시 모든 방법이 한번이상씩 사용되어야하지만, 이는 불가능하므로. 2,3번을 총 3번쓰는 경우만 존재한다. # m 이 7보다 클땐(3번이상이동가능):무조건 각 방법4번써야하므로 답은 4.
 # 그외에의 조건에서는 2,3번중 하나를 사용하기에(무조건2칸이동) m+1칸의 여유가필요하고 2칸씩이동하므로 2로 나눈 몫만큼만 이동가능하다.
    result = min(4,(m+1) // 2)  
else: #세로가 3칸이상이라 두칸 위아래로 가능하므로. 
  if m <= 6: #가로가 6이하이면, 4번사용하며 모든 방법을 사용가능하다.
    result = min(4, m) # 모두 사용한 4번이던지, 1,4번만 이용한 m만큼이 최대.
  else:
    result = m - 2 #가로가 7이상이라면, 모든 방법을 쓸수있어야하고, 1,4번만 사용하는게 한칸씩 오른쪽으로 이동하며 가장 빡빡하게 제일 많이 방문할수있으므로, 2가지 케이스를 뺀만큼을 출력. 

print(result)