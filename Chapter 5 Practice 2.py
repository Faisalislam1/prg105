

def main():
    number = int(input("Enter a whole number between 20 and 100: "))
    while 20 > number or number > 100:
        number = int(input("Enter renter whole number between 20 and 100: "))
    if two(number):
        print(number,"is devisable by two")
    else:
        print(number,"Is not devisable by two")
    if three(number):
        print(number, "is devisable by three")
    else:
        print(number, "Is not devisable by three")
    if five(number):
        print(number, "is devisable by five")
    else:
        print(number, "Is not devisable by three")


def two(number):
    if number % 2 == 0:
        return True
    else:
        return False


def three(number):
    if number % 3 == 0:
        return True
    else:
        return False


def five(number):
    if number % 5 == 0:
        return True
    else:
        return False


main()
