marques = ['bmw', 'audi', 'mercedes-benz', 'gm', 'ford']

print(
    f'The last brand in our list is {marques[-1].title()}.\nThe second to last brand in the list is {marques[-2].upper()}.\nThe first brand in the list is {marques[0].upper()}.')


marques.append('chevrolet')
marques[4]='bronco'

print(
    f'The last brand in our list is {marques[-1].title()}.\nThe second to last brand in the list is {marques[-2].upper()}.\nThe first brand in the list is {marques[0].upper()}.')

marques.insert(0,'lexus')
print(f'The first element is now {marques[0].title()} and the second one becomes {marques[1].upper()}')

print(marques)

del marques[0]

print(marques)

print(marques.pop())
print(marques)

print(marques.pop(1))
print(marques)

marques.remove('gm')
print(marques)

marques.sort()
print(marques)

marques.sort(reverse=True)
print(marques)

print(sorted(marques))

print(f'The total length of the list is now {len(marques)}.')