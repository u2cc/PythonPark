from _decimal import Decimal

a = input('Please give the first operand for multiplication:')
b = input('Please give the second operand for multiplication:')

product = Decimal(a)*Decimal(b)

print(f'The answer is {product}')