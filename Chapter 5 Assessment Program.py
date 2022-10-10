import math


def main():
    number = 0
    while number != 5:
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
            width = float(input("Enter the width of the rectangle in cm:"))
            height = float(input("Enter the height of the rectangle in cm"))
            rectangle(width,height)

        elif number == 2.00:
            width = float(input("Enter the width of the Triangle in cm:"))
            height = float(input("Enter the height of the Triangle in cm"))
            triangle(width,height)

        elif number == 3.00:
            width = float(input("Enter the width of the rectangle in cm:"))
            
            square(width)
    
        elif number == 4.00:
            radius = float(input("Enter the radius of Circle"))
            
            circle(radius)

        elif number == 5.00:
            print("this is not a valid number \n Goodbye")


def rectangle(width,height):
    area = width*height
    print("Your area is", area)


def triangle(width,height):
    
    area = (width*height)*.5
    print("Your area is", area)


def square(width):
    area = (width*width)
    print("Your area is", area)


def circle(radius):
    area = math.pi*(radius*radius)
    print("Your area is", area)


main()
