a, b = input().split()
w = int(a)
h = int(b)
n = int(input())
array = [[0] * h for _ in range(w)]

for i in range(n):
    data = input().split()
    long = int(data[0])
    direct = int(data[1])
    x = int(data[2])
    y = int(data[3])

    if direct == 0:
        for j in range(1, long + 1):
            array[x - 1][y - 2 + j] = 1
    elif direct == 1:
        for j in range(1, long + 1):
            array[x + j - 2][y - 1] = 1

for i in range(w):
    for j in range(h):
        print(array[i][j], end=" ")
    print(end='\n')


#shorter
a, b = input().split()
w = int(a)
h = int(b)
n = int(input())
array = [[0] * h for _ in range(w)]

for i in range(n):
    l,d,x,y = input().split()

    if int(d) == 0:
        for j in range(1, int(l) + 1):
            array[int(x) - 1][int(y) - 2 + j] = 1
    elif int(d) == 1:
        for j in range(1, int(l) + 1):
            array[int(x) + j - 2][int(y) - 1] = 1

for i in range(w):
    for j in range(h):
        print(array[i][j], end=" ")
    print(end='\n')
