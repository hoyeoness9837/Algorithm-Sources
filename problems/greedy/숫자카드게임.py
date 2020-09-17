## Question ##
# In N * M 2D array, pick a Nth column and check its lowest number of that row. that number should be largest among other colums. find the number.
# INPUT = N: 3 M: 3 | 3 1 2 | 4 1 4 | 2 2 2
# ANSWER = 2


## My Answer
n,m = map(int, input().split())
num =[]

for i in range(n):
  data = list(map(int, input().split()))
  data.sort()
  smallest = data[0]
  num.append(smallest)

num.sort()
largest = num[n-1]
print(largest)

## Solution 1
n,m = map(int, input().split())
result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data)
  result = max(result, min_value)

print(result)

## Solution 2
n,m = map(int, input().split())
result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_value = 10001
  
  for a in data:
    min_value = min(min_value, a)
  
  result = max(result, min_value) 

print(result)

## Notes ##
# use min, max, they are useful
# dont have to return in the loop, just store in var and print it outside the function.
# result = max(result, min_value)가 반복되면서 반복적으로 들어오는 min_value중 최대값을 result에 갱신해 저장해놓는다.