


while True:
    first_number = input("Enter a number: ")
    second_number = input("Enter second number: ")

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Text is not valid. Please enter a number.")
    else:
        print(answer)
