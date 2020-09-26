# 'q'가 입력될 때까지 입력된 문자를 줄을 바꿔 한 줄씩 출력한다.
# q 도 포함한다.

#
a = list(map(str, input().split()))

for i in range(len(a)):
  print(a[i])
  if a[i] == "q":
    break

#solution
a=input().split()

for c in a :
    print(c)
    if c=='q' :
        break