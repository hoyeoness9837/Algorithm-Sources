####Functions####

def add(a, b):
    return a+b
print(add(b=10, a=5))
#result = 15

#global variable
a = 5
def func():
    global a
    a += 1
for i in range(10):
    func()
print(a)
#result = 5 + 10(1) = 15


#lambda
print((lambda a, b: a - b)(10, 3))
# result = 10 - 3 = 7