data = input().split("-")
result = 0
for i in data[0].split("+"):
  result += int(i)

for i in data[1:]:
  for j in i.split('+'):
    result -= int(j)

print(result)

# a+b+c-d+c-e+f
# 괄호를 넣는곳이 - 기준으로, 나머지는 더해주되
# 덧셈끼리 묶어서 더해준다음 빼주어야함.