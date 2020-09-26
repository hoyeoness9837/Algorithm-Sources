# 입력된 16진수에 1~F까지 순서대로 곱한, 16진수 구구단을 줄을 바꿔 출력한다.
# 계산 결과도 16진수로 출력해야 한다.
n = input()

for i in range(1,16):
  result = str(hex(int(n,16)*i))[2:] # 16진수를 10진수로 해석한다음 i와 곱한후 다시 16진수로 포맷한것을 str앞두자리는 떨어트리고 저장
  result = result.upper() #소문자는 대문자로 저장
  i=hex(i)[2:] # 1-16사이의 10진수수를 16진수로 표현.
  print(n+"*"+i.upper()+"=",result)