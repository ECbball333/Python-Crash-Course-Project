

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

#Letting the User Choose When to Quit the Program
#message = ""
#while message != 'quit':
#    message = input(prompt)

#    if message != 'quit':
#        print(message)


#Using a flag to stop a program
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(f"\n{message}")