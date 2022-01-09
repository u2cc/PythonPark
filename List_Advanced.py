names = ['bob', 'alice', 'john', 'jane']

i=0
for name in names:
    print(name.capitalize())
    print(f'I am still in the loop {i}.')
    i=i+1

print('Loop has ended.')

range_object = range(1, 5)
print(range_object)

list_of_numbers = list(range_object)

for value in range_object:
    print(value)

print(list_of_numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

digits=list(range(0,10))
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)

#slicing a list
brands = ['NIKE','DELL','Apple','Microsoft']
print(brands[0:3])
print(brands[:3])
print(brands[1:])
print(brands[-2:]) #prints last two using negative numerics

for brand in brands[-2:]:
    print(brand)

my_cars = ['Lexus','Toyota']
my_friend_cars = my_cars[:]

my_cars.append('Ford')
my_friend_cars.append('Ram')

print(f'My cars: {my_cars}')
print(f'\nMy friend\'s cars: {my_friend_cars}')