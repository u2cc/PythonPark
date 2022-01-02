message = '"Hellp Python world!" - A variable'
#usages of both single quote and double quote can reduce the dependency on escape character

"""This is a multi-line comment
surrounded by triple quotation marks"""

print(message)

title = 'this is Supposed to be a title but with cases Going haywire'

print(title.title())
print(title.upper())
print(title.lower())

#Formating syntax after Python 3.6 inclusive
first_name = 'Jim'
last_name = 'Green'
print(f"Name: {first_name} {last_name}")

#Formatting syntax before Python 3.6
print("Name: {} {}".format(first_name, last_name))

#tab and whitespaces
print("Newline will commence below\nTab will be inserted here\tI am after the tab\nI should be on a newline")

#stripping whitespaces
left_with_whitespace = "   Lefty"
right_with_whitespace = "Righty   "
both_end_whtiespace = "   Ambidextrous   "

print(f"Lefty: {left_with_whitespace}.\nLStripped Lefty: {left_with_whitespace.lstrip()}.")
print(f"Righty: {right_with_whitespace}.\nRStripped Righty: {right_with_whitespace.rstrip()}.")
print(f"Ambidextrous: {both_end_whtiespace}.\nStripped Ambidextrous: {both_end_whtiespace.strip()}.")

#Escape Character \
print("This string is surrounded by double quotes and carries double quotes \"\" itself therein")


