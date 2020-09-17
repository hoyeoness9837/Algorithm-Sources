#### collections ####
## deque
# use popleft(), popright() or appendleft(), appendright() to manage ends of list.
# beacuse basic append and pop are only responsible for the last value in list.

from collections import deque
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
print(list(data))
# result = [1, 2, 3, 4, 5]

data.popleft()
data.append(6)
print(list(data))
# result =  <-pop- [2, 3, 4, 5, 6] <-append-

data.pop()
data.appendleft(1)
print(list(data))
# result = -append->[1, 2, 3, 4, 5]-pop->

data.pop()
data.popleft()
print(list(data))
# result = [2, 3, 4]


## Counter
# it is useful for counting strings & something that is not in order. use bisect for finding numbers!
from collections import Counter
counter = Counter(['red','red','blue','black','white','green','red'])
print(counter['red'])
#result = 3
print(dict(counter))
#result = {'red': 3, 'blue': 1, 'black': 1, 'white': 1, 'green': 1}
