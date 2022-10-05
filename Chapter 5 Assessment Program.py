import math


def main():
    print("This program will find the area of a shape for you.")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Square")
    print("4. Circle")
    print("5. Quit")
    number = int(input("What shape would you like to pick"))
    while 0 < number and number > 5:
        number = int(input("Enter renter whole number between 1 and 5: "))
    if number == 1.00:
        Rectangle()

    elif number == 2.00:
        Triangle()

    elif number == 3.00:
        Square()

    elif number == 4.00:
        Circle()

    elif number == 5.00:
        print("this is not a valid number \n Goodbye")


def Rectangle():
    width = float(input("Enter the width of the rectangle in cm:"))
    hight = float(input("Enter the hight of the rectangle in cm"))
    area = width*hight
    print("Your area is", area)


def Triangle():
    width = float(input("Enter the width of the Triangle in cm:"))
    hight = float(input("Enter the hight of the Triangle in cm"))
    area = (width*hight)*.5
    print("Your area is", area)


def Square():
    width = float(input("Enter the width of the rectangle in cm:"))
    area = (width*width)
    print("Your area is", area)


def Circle():
    radius = float(input("Enter the radius of Circle"))
    area = math.pi*(radius*radius)
    print("Your area is", area)

main()



