def greet_user(username):
    print(f"Hello, {username.title()}!")


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