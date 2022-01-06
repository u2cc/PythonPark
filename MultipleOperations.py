from decimal import Decimal

g = input('Give the first operand for addition: ')
c = input('Give the second operand for addition: ')
o = input('Give the third operand for multiplication: ')
p = input('Give the fourth operand for multiplication: ')
sum = Decimal(g)+Decimal(c)

product = Decimal(o)*Decimal(p)

print(f'The answer of addition is {sum}. The answer of multiplication is {product}.')