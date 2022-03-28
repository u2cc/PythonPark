cars = ['subaru','bmw','audi','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

audi = 'audi'
print(audi=='audi')

#test string equality case insensitive
print(audi.casefold()=='AUDI'.casefold())

#test inequality
requested_topping ='mushrooms'
if (requested_topping.casefold()!='anchovies'.casefold()):
    print('It is not anchovies!')

ages = [16, 17, 18,19,20,21]
for age in ages:
    if age<18:
        print(f'You are too young at age of {age}.')
    if age>=18:
        print(f'You are an adult at age of {age}.')


age_0 = 22
age_1 = 18

print(age_0>=21 and age_1 >=21)
print(age_0>=21 or age_1 >=21)

#check list member existence
print('Subaru'.casefold() in cars)
print('Subaru'.upper() in cars)
print('Lexus'not in cars)

for value in range(1,10):
    if value<2:
        print(f'value is too small: {value}')
    elif value<5:
        print(f'value is not too big: {value}')
    else:
        print(f'It is a big value: {value}')

items = []
if items:
    print(f'List content: {items}')
else:
    print('There is no item in the list.')

elements = ['hydrogen','nitrogen']
if not elements:
    print('There is no element in the list.')
else:
    print(f'List content: {elements}')
