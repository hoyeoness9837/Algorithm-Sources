####Set####
# No Overlap, Non-iterable, not subscriptable
# useful for checking if any data have been appeared

data = set([1, 1, 2, 3, 4, 4, 4, 5])
print(data)
#result = {1, 2, 3, 4, 5}   the overlapping numbers are removed.
data = {1, 1, 2, 2, 3, 4, 5, 6, 7, 7, 7}
print(data)
#result = {1, 2, 3, 4, 5, 6, 7} the overlapping numbers are removed.


a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])
print(a|b)
#result = {1, 2, 3, 4, 5, 6, 7}
print(a&b)
#result = {3, 4, 5}
print(a-b)
#result = {1, 2}
print(b-a)
#result = {6, 7}

a.add(8)
a.update([0,9,10])
a.remove(4)
print(a)
#result = {0, 1, 2, 3, 5, 8, 9, 10}  the numbers are aligned.

first = a[0]
print(first)
#result = TypeError: 'set' object is not subscriptable