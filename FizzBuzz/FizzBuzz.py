while True:
    number = int(input("Enter the number: "))
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    check_again = input("Would you like to continue? Type 'y' to continue or 'e' to exit: ")
    if check_again == 'y':
        continue
    elif check_again == 'e':
        print("Thank you. See you next time, bye!")
        break
    else:
        print("You have two options: 'y' to continue and 'e' to exit.")