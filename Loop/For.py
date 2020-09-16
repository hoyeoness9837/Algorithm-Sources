#### For loop####
result = 0

for i in range(1, 10):
    result += i
print(result)
#result= 1+2+3+4+5+6+...+9 = 45


#continue: The loop goes back to the starting point.
score = [90, 85, 77, 65, 97]
black_list = {2, 4}

for i in range(len(score)):
  if i + 1 in black_list:
    continue
  if score[i] >= 80:
    print(f"{i+1}th student is pass")
#result = 1th student is pass  5th student is pass


#2D loops
for i in range(1,10):
    for j in range(1,10):
        print(f"{i}x{j} = {i*j}")
#result =  1x1 = 1...9x9 = 81