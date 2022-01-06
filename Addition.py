from decimal import Decimal

g = input('Give the first operand for addition: ')
z = input('Give the second operand for addition: ')
c = input('Give the third operand for addition: ')
a = input('Give the fourth operand for addition: ')
b = input('Give the fifth operand for addition: ')
r = input('Give the sixth operand for multiplication: ')
result= (Decimal(g)+Decimal(z)+Decimal(c)+Decimal(a)+Decimal(b))*Decimal(r)
print(f'the answer is {result}')

