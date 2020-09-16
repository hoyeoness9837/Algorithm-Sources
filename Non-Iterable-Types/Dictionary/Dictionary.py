####Dictionary####
##similar to obejct, has key and value, so it is non-iterable type.
##internally uses Hash Table. Operates faster than List
data = dict()
data['apple'] = 'red'
data['grape'] = 'purple'
data['orange'] = 'orange'
data['banana'] = 'yellow'
print(data)

#result = {'apple': 'red', 'grape': 'purple', 'orange': 'orange', 'banana': 'yellow'}

if 'apple' in data:
  print('true')
#result = true

key_list = data.keys()
print(key_list)
#result = dict_keys(['apple', 'grape', 'orange', 'banana'])

value_list = data.values()
print(value_list)
#result = dict_values(['red', 'purple', 'orange', 'yellow'])

for value in value_list:
  print(value)
#result = red purple orange yellow
