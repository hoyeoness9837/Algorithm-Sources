##stack
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(14)
stack.pop()

print(stack) # [5, 2, 3, 1]
print(stack[::-1]) #[1, 3, 2, 5]

##queue
from collections import deque

from collections import deque

queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(list(queue)) # [3, 7, 1, 4]
queue.reverse()
print(list(queue)) # [4, 1, 7, 3]

##recursive function 1
def recursive_fuction(i):
  if i == 100:
    return
  print("in", i, 'th recursive function,', 'calling',i + 1,'th recursive function.' ) # 1-99, 1-100
  recursive_fuction(i + 1) 
  print(i, 'th,here, closing.') # 1-99
recursive_fuction(1)


##recursive function 2
#factorials in two ways
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i # result = 1 * 2 * 3 * 4 * 5
    return result

#this is simpler.
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1) # n! = n*(n-1)!

print(factorial_iterative(5))
print(factorial_recursive(5))

#####DFS - STACK/RECURSIVE

#Adjacency Matrix
INF = 999999999
graph = [
  [0,7,5],
  [7,0,INF],
  [5,INF, 0]
]
print(graph)
#Adjacency List
graph=[[] for _ in range(3)]

graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))
graph[2].append((0,5))

print(graph)