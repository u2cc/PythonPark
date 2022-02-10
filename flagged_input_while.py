

continue_flag = True
message=""
while continue_flag == True:
    message = input("Type \"quit\" to quit the program otherwise this program will repeat your input:\n")
    if message!='quit':
     print(message)
    else:
        continue_flag = False