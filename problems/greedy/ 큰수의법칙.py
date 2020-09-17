## Question ##
# What is the largest number you can make as adding up M times with given numbers in an array with lenght of N, if a certain number cannot be used K times in a row.
# INPUT = 5 8 3  |  2 4 5 4 6
# ANSWER = 46


## My Answer
[M, K] = [8, 3]
numbers = [2, 4, 5, 4, 6]
N = len(numbers)

a = sorted(numbers, reverse=True)
first_largest = a[0]
second_largest = a[1]
r = M/(K+1)

result = int(r*(first_largest*K + second_largest))
print(result)


## Solution 1
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1

  if m == 0:
    break
  result += second
  m -= 1

print(result)


## Solution 2
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1))*k
count += m % (k+1)

result = 0
result += first*(count)
result += second*(m-count)

print(result)


## Notes ##
# get inputs map(int, input().split())
# double check if you are using  '/', consider if you need '%'
# test 4 8 4, [1,8,9,2], mine returns 70, solution returns 71
