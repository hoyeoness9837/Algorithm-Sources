#두 정수를 비트단위(bitwise)로 and 계산을 수행한 결과를 10진수로 출력한다.
a, b = input().split()
x = int(a)
y = int(b)
z = '{0:b}'.format((x & y))

result = int(z, base = 2)

print(result)

##solution
a,b=input().split()
x=int(a)
y=int(b)
print(x&y)