# a부터 입력한 문자까지 순서대로 공백을 두고 출력한다.
end = ord(input())
a = 97

for i in range(a, end + 1):
    print(chr(i))
    i =+ 1


# solution
c=input()
n=ord(c)
i=ord('a')

while i<=n :
    print(chr(i), end=' ')
    i+=1