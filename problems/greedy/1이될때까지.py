## Question ##

# 어떠한 수 N이 1이 될때까지 다음 두 과정중 하나를 선택하여 수행함. 단 두번째 연산은 N이 K로 나누어 떨어질때만 선택가능 1. N에서 1을뺀다,  2.N을 K로 나눈다.  1또는2번의 과정을 수행해야하는 최소횟수를 구하시오.
# INPUT = 102 10
# ANSWER = 4 (102 -> 101, 101 -> 100, 100 -> 10, 10 -> 1)


## My Answer - wrong!!
n, k = map(int, input().split())
result = 1
m = (n % k)

while True:
  if n == k:
    break
  else:
    if n == 1:
      break
    n = (n // k)
    result += 1

answer = result + m
print(answer)

## Solution 1
n, k = map(int, input().split())
result = 0

while n >= k:
  while n % k !=0:
    n -= 1
    result += 1
  n //= k
  result += 1

while n > 1:
  n -= 1
  result += 1

print(result)

## Solution 2
n, k = map(int, input().split())
result = 0

while True:
  target = (n//k)*k
  result += (n - target)
  n = target
  if n < k:
    break
  result += 1
  n //= k

result += (n - 1)
print(result)

## Notes ##
# Use 'while' when you have certain condition.
# You can use '//='
# n//k = 0 when  n < k 
