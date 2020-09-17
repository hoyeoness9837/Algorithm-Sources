####HEAPQ####
import heapq


##heap sort## using heappush and heappop
def heapsort(iterable):
    h = []
    result = []
    #all values are now pushed in heap in orders (lower-higher)
    for value in iterable:
        heapq.heappush(h, value)
    # all values are now popped and appended in result.
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
#result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


##heap sort## using heappush and heappop --- reversing version
def heapsort(iterable):
    h = []
    result = []
    #all values are now pushed in heap in orders (most negative - closer to zero) -9,-8,...-1
    for value in iterable:
        heapq.heappush(h, -value)
    # all values are now popped and appended in result. -1 * (-9, -8, -7, ..., -1) => 9, 8, 7, ..., 1
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
#result = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]