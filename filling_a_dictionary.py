responses = {}

continue_while_loop = True

while continue_while_loop:
    name = input("What is your name?\n")
    response = input("May I know your favorite food, please?\n")

    responses[name] = response

    repeat = input("Do you want another person to answer?\n")
    if repeat.casefold() == 'no':
        continue_while_loop = False

print("\n ----- result -----")
for name, response in responses.items():
    print(f"{name}'s favorite food is {response}.")