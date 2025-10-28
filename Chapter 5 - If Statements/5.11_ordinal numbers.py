numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1:
        print("1st")
    if number == 2:
        print("2nd")
    if number == 3:
        print("3rd")
    elif number >= 4:
        print(f"{number}th")
