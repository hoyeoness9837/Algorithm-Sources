####Itertools####
from itertools import permutations, product, combinations_with_replacement, combinations
data = ['A', 'B', 'C']


##permutations##
result = list(permutations(data, 3))
print(result)
#result = [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]


##prdocut## AA,BB,CC: ok, AB != BA
result = list(product(data, repeat=2))
print(result)
#result = ('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]


##combinations_with_replacement##   AA,BB,CC: ok, but BA = AB
result = list(combinations_with_replacement(data, 2))
print(result)
#result = [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]


##combinations##   AA,BB,CC: not allowed, AB != BA
result = list(combinations(data, 2))
print(result)
#result = [('A', 'B'), ('A', 'C'), ('B', 'C')]

result = list(combinations(data, 3))
print(result)
#result = [('A', 'B', 'C')]
