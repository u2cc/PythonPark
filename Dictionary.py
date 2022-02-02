alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0['color'] = 'red'

print(alien_0)
print(f"The color of alien_0 is {alien_0['color']}.")

if alien_0['color'] == 'red':
    alien_0['color'] = 'blue'
    print(f"Alien color now changed to {alien_0['color']}.")
elif alien_0['color'] == 'white':
    alien_0['color'] = 'black'
    print(f"Alien color now changed to {alien_0['color']}.")
else:
    print(f"Alien color was not changed and is {alien_0['color']}.")

#delete a key-value pair
del alien_0['points']
print(alien_0)

extended_dictionary = {
    'James':'Java',
    'Wendy':'C',
    'Yiding':'Python',
    'Eason':'.NET',   #Good practice to include a comma for the last entry for ease of adding new pairs
    }

language_wendy = extended_dictionary['Wendy'].title()
print(f"Wendy's favorite language is {language_wendy}.")

#In case the key is non-existent in the dictionary, we can use get method
language_jim = extended_dictionary.get('jim','no such entry')


for key, value in extended_dictionary.items():
    print(f"\nKey: {key}")
    print(f"value:{value}")

#use more meaningful names for key and value variables
for name, language in extended_dictionary.items():
    print(f"\nName: {name}")
    print(f"language: {language}")

friends = ['James','Wendy']
for name in extended_dictionary: # can also use extended_dictionary.keys() for better readability
    print(f"\nKey: {name}")
    if name in friends:
        print(f"My friend {name}'s favorite language is {extended_dictionary[name]}.")

for name in sorted(extended_dictionary, reverse=True):
    print(name)