print('\n')

caprese = 'tomato mozzarella basil'
caprese_list = caprese.split(' ')
print('Caprese ingredients are:', caprese_list[0], caprese_list[1], caprese_list[2])

print('\n')

x = '1,2,3'
y = x.split(',')
print(y)

print('\n')

a,b,c = x.split(',')
print(a)
print(b)
print(c)

print('\n')

str = 'Caprese ingredients are: tomato mozzarella basil.'
print(str.split())
print(str.split('i',1))
print(str.split('w'))

print('\n')

s = "Tokyo,Boston,London,New York,Los Angeles"
cities = s.split(",")
for city in cities:
    print(city)
