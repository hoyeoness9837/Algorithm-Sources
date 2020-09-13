####LIST####
a = list()
a = []
a = [i for i in range(10)]
print(a)
#result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[-1])
#result = 9

print(a[0:-1])
#result = [0, 1, ..., 8]

print(a[2:6])
#result = [2, 3, 4, 5]

n = 10
a = [0] * 10
print(a)
#result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

a = [i for i in range(10) if i % 2 == 0]
print(a)
#result = [0, 2, 4, 6, 8]

a = [i for i in range(10) if i % 2 == 1]
print(a)
#result = [1, 3, 5, 7, 9]

n = 4
m = 3
a = [[0] * m for _ in range(n)]
print(a)
#result = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

a = [8, 1 ,3 ,3 ,3 ,3]
a.append(61)
print(a)
#result = [8, 1, 3, 3, 3, 3, 61]

a.insert(1, 93)
print(a)
#result = [8, 93, 1, 3, 3, 3, 3, 61]

a.sort()
print(a)
#result = [1, 3, 3, 3, 3, 8, 61 ,93]

a.sort(reverse=True)
print(a)
#result = [93, 61, 8, 3, 3, 3, 3, 1]

a.reverse()
print(a)
#result = [1, 3, 3, 3, 3, 8, 61 ,93]

a.remove(3)
print(a)
#result = [1, 3, 3, 3, 8, 61]

print(a.count(3))
#result = 3

## DO NOT OVERUSE append(), insert(), and remove(). their bigO is O(N). Instead use following one.
remove_set=[3]
nothree = [i for i in a if i not in remove_set]
print(nothree)
#result = [1, 8, 61, 93]