#Nicola Batty
#04/02/2015
#Files R&R Task 5

def number_too_big():
    print("The number you have chosen is too big. Please try again.")

def number_too_small():
    print("The number you have chosen is too small. Please try again.")

def not_a_number():
    print("That is not a number. Please try again.")
    what_number()

def print_number(number):
    print(number)

def input_number():
    number = int(input("please input number from 1 to 100: "))
    return number

def loop_numbers(right):
    while not right:
        number = input_number()
        if number < 1:
            number_too_small()
        elif number > 100:
            number_too_big()
        else:
            print_number(number)
            right = True

def what_number():
    try:
        right = False
        loop_numbers(right)
    except ValueError:
            not_a_number()
