n = int(input())
list = [5, 3]
count1 = 0
count2 = 0

if n % 3 == 0 or n % 5 == 0:
  count1 = n//3
  for bag in list:
      count2 += n // bag
      n %= bag
  if n !=0:
    print(count1)
  elif n == 0: 
    print(count2)
else:
  print(-1)

11을 입력하면 첫 조건문에서 만족하지 못하므로 -1이 되는데, 그외에는 괜찮다.

##정답##
suger = int(input())
bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else:
  print(-1)
