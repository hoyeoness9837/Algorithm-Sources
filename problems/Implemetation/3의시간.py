## Question ##

# Count how many times of numbers in range of time between 00:00:00 and  N:59:59 are including 3 in the time?
# INPUT = 5
# ANSWER = 11475


## My Answer
n = int(input())
count = 0
m=1
s=1

for h in range(n):
  if 3 in range(1,n):
    count+= 1
    n += 1
    for m in range(0,60):
      m=+1
      if 3 in m:
        count+= 1
        for s in range(0,60):
          s+=1
          if 3 in s:
            count+= 1
  
result = count
print(result)

## Solution 1
n = int(input())
count = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
          if '3' in str(h) + str(m) + str(s):
            count+= 1
  
result = count
print(result)


## Notes ##
#1. for x in range... x will automatically increase by 1.
#2. you cannot do checking if int type is in a list. always make it into string first.