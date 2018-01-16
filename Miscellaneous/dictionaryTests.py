#! python3

# animals = ['cats', 'lizards', 'bats', 'hawks']
# creatures = ['bats', 'lizards', 'cats', 'hawks']

# print(animals == creatures)
# false

animals = {'cats': 'siamese', 'lizards': 'monitor', 'bats': 'fruit', 'hawks': 'red-tailed'}
creatures = {'hawks': 'red-tailed', 'cats': 'siamese', 'lizards': 'monitor', 'bats': 'fruit'}

# print(animals == creatures)
# true
# unlike lists, dictionaries are not ordered.

# print(animals['cats'])

# keys, values, items.
# they cannot be modified and do not have an append() method.
# can be used in for loops.

for v in animals.values():
    print(v)
    # prints in order as typed.

for k in animals.keys():
    print(k)
    # prints in reverse as typed.

for i in animals.items():
    print(i)
    # prints 4th, 2nd, 3rd, 1st

if 'monitor' or 'iguana' in animals.values():
    print('True')
else:
    print('False')

# can't have key with 2 values?

if 'monkey' not in animals:
    animals['monkey'] = 'gelada'
    print(animals)
