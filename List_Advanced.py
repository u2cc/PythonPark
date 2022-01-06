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

