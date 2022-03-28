def greet_user(username):
    print(f"Hello, {username.title()}!")

# stuff only to run when not called via 'import' here
if __name__=='__main__':
    greet_user("JAMES")

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type.lower()}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

describe_pet(pet_name='harry', animal_type='hamster')

def describe_car(brand, type = 'SUV'):
    print(f"\nI have a car of type {type}.")
    print(f"The car's make is {brand.upper()}.")

describe_car("buick")
describe_car('Toyota','sedan')

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name

name = get_formatted_name('James', 'Chen')
print(name)

name = get_formatted_name("George", 'Bush', 'W')
print(name)

name = get_formatted_name(middle_name='W', first_name='George', last_name = 'White')
print(name)

"""demo inappropriate use of positional argument after out of order keyword arugment"""

"""
name = get_formatted_name(middle_name='W', 'George', 'White')
print(name)
"""

print(''==None)

name = get_formatted_name("George", 'Bush', None)
print(name)


"""A function returning a dictionary"""
def build_person(first_name, last_name, age=None):
    person = {'first': first_name.title(), 'last':last_name.title()}
    if age:
        person['age']=age
    return person

musician = build_person('jimmy','hendrix', 35)
print(musician)

musician = build_person(age=38, first_name='jimmy',last_name='hendrix')
print(musician)

"""Passing a list"""
def greetUser(names):
    for name in names:
        msg = f'Hello, {name.title()}.'
        print(msg)

usernamelists = ['Jimmy Hendrix', 'Eric Johnson', 'Joe Satriani']
print(greetUser(usernamelists))

"""Modifying a list in function"""
unprocessed_items = ['A', 'B', 'C']
def processItems(list):
    processed_items = []
    while list:
        popped_item = list.pop(0)
        print(f'Processing item {popped_item}')
        processed_items.append(popped_item)

    for item in processed_items:
        print(f'Item processed: {item}')

processItems(unprocessed_items)

"""Arbitrary number of arguments"""
def printAllToppings(*toppings):
    print(toppings)
    print('Printing toppings in a list:')
    for topping in toppings:
        print(topping)

printAllToppings('beef', 'sausage', 'onion')

"""Arbitrary keyword arguments using dictionary as an input parameter"""
def buildProfile(first, last, **userinfo):
    userinfo['first'] = first.title()
    userinfo['last'] = last.title()
    print(userinfo)

buildProfile('jimmy','hendrix',location='USA', age = 35)

buildProfile(location='USA', age = 45, first='Richard',last='Hammond')
