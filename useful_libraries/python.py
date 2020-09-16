#dont need to import anything
#print(), min(), max()

#eval() : return calculated int if numbers were given as string.
result = eval("5+7")
print(result)
# result = 12

#sorted(), reverse, x:x[1] indicates their values.
result = sorted([('apple', 10), ('banana', 1), ('blueberry', 5),
                 ('strawberry', 7), ('pear', 3)], key=lambda x: x[1], reverse=True)
print(result)
# result = [1, 3, 5, 7, 9]
