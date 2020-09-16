#### Conditional####
score = 85
if score >= 80:
  pass
else:
  print("Score is lower than 80")
print("End Program")
#result = "End Program"

#you can write this way if it's only one line.
result = "Success" if score >= 80 else "Fail" 
print(result)
#result = "Success"


a = [1, 2, 3, 4, 5, 6, 7]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set] #[  "keep" i   /    for i    /   in a   /   if i   not in remove_set    ]
print(result)
#result = [1, 2, 4, 6, 7]