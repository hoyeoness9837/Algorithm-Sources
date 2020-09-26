# 1, 2, 3 ... 을 순서대로 계속 더해나갈 때,
# 그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램을 작성해보자.
a = int(input())
i = 1
sum = 0
while sum < a:
  sum += i
  i += 1
  
print(sum)