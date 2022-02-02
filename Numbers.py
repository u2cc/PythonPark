from decimal import Decimal
#https://docs.python.org/3/library/decimal.html

sum = 2+3
difference = 3-2
product = 2*3
quotient = 3/2

print(sum)
print(difference)
print(product)
print(quotient)

#base**exponent=power
power = 3**2
print(power)

#order of operation
result_of_natura_order = 2 + 3 * 4
result_of_pemdas = (2 + 3) * 4
print(result_of_natura_order)
print(result_of_pemdas)

#arbitrary number in result
result_with_arbitrary_number = 0.2 + 0.1
print(result_with_arbitrary_number)

a = Decimal("0.2")
b = Decimal('0.1')
print(a+b)

#underscore in numbers
speed_of_light = 299_792_458
print(speed_of_light)

#multiple assignment
x, y, z = 0, 0, 0
print(f'x:{x}\ny:{y}\nz:{z}')

#constant
ABSOLUTE_ZERO_IN_CELSIUS = -273.15
print(ABSOLUTE_ZERO_IN_CELSIUS)


