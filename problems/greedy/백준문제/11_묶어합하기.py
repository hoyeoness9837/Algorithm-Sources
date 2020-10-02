#[-3,-2, 0,1,2,3] 이라는 숫자가 있다면, 두개씩 묶어 합이 최대가 되도록한다
#(-3)*(-2), 0, 1, (2*3) 으로 만들고 더 해주면 가장 큰 값인 13을 갖는다.
#함정: 1) 0을 포함한 음수는 작은 수 부터 묶는다. 3) 1보다 큰 수는 큰 수부터 묶는다. 2) 숫자가 1인 경우에는 묶지 않는다.
#예 : 1,1,1,1 이렇게 주어질땐 4가 정답, -1,0,2,3 일땐 -1과 0 이 묶여 0 으로 바꿔주는게 최대.

#내 답
n = int(input())
arr = []
d = 0
for _ in range(n):
  arr.append(int(input()))
arr = sorted(arr)
for i in range(1,n):
  if abs(arr[i-1]) > 1:
    d += arr[i-1] * arr[i]
  else:
    d += arr[i-1]
print(d)


#####정답#####
#input = 8 | -8 1 -1 0 2 6 4 -9
import sys
N = int(sys.stdin.readline()) 
data = [int(sys.stdin.readline()) for _ in range(N)]

neg = []
pos = []
result = 0

for num in data:
    if num <= 0:  #입력된 숫자들중 0과 음수들에 대해선,
        neg.append(num) #네거티브 리스트에 넣어줌.
    elif num == 1:
        result += 1  #숫자가 1인 경우에는 묶지 않는것이 항상 이득이므로, 미리 답에 따로 계산하여 둔다. 즉, 1만있다면 다 더해버리는게 정답.
    elif num > 1: #그 외 1보다 큰 양수들에 대해선
        pos.append(num) #포지티브 리스트에 넣어줌

# 목적에 맞게 정렬 절대값이 큰수가 왼쪽으로.
neg.sort() # -9, -8, -1, 0
pos.sort(reverse=True) # 6, 4, 2

# 1) 작은 수부터 차례대로 묶는다. 
for i in range(0, len(neg), 2): # ( start, end, by )
    if i + 1 < len(neg): # 범위를 벗어나지 않는조건의 음수에 대해선, i+1 = 1,2,3 < 4 , (-9 * -8) = 72, (-1 * 0)= 0
        result += neg[i] * neg[i + 1]
    else: # 묶이지 못한 음수들은 더해준다.
        result += neg[i]

# 2) 큰 수부터 차례대로 묶는다.
for i in range(0, len(pos), 2):
    if i + 1 < len(pos):
        result += pos[i] * pos[i + 1] # 6 * 4 = 24, 2
    else:
        result += pos[i]

print(result) # 1 + 72 + 0 + 24 + 2 = 99