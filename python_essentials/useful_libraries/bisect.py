#### BYSECT ####

## bisect_left and bisect_right gets the index as if it tries to insert where that matching values at. keeps the order is point.
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]  # in which list
x = 4  # which value
print(bisect_left(a, x))
# result = 2 [1(i=0), 2(i=1), **(i=2), 4(i= 2->3), 4(i= 3->4), 8(i= 4->5)]
print(bisect_right(a, x))
# result = 4 [1(i=0), 2(i=1), 4(i=2), 4(i=3), **(i=4), 8(i= 4->5)]


##also useful if you are trying to find a number of certain value in a certain range in an organized list.
def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# returns how many 3s in a
print(count_by_range(a, 3, 3))
# result = 4  [1, 2, (**), 3, 3, 3, 3, (**), 4, 4, 8, 9] =>  6 - 2 = 4

# returns how many values between at most left 1 and at most right 3
print(count_by_range(a, 1, 3))
# result = 6   [(** i = 0), 1, 2, 3, 3, 3, 3,(** i = 6), 4, 4, 8, 9] =>  6 - 0 = 6

