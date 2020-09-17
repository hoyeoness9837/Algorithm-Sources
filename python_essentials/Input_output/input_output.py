###INPUT and OUTPUT###

#BASIC
#memorize this ... list(map(int, input().split()))
n = int(input())
data = list(map(int, input().split()))
data.sort(reverse=True)
print(data)
#5
#65 90 75 34 99
#result = [99, 90, 75, 65, 34]

n, m, k = map(int, input().split())
print(n, m, k)
# 3 5 6
# result = 3 5 6

#for better time saving purpose use ... sys.stdin.readline().rstrip() instead of input()
import sys
data = sys.stdin.readline().rstrip()
print(data)
# hello world
#result = hello world
