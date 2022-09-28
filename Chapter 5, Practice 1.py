
MC = "a"
R = "b"
S = "c"
GC = "d"
G = "e"


def main():
    print("Select one of the menu options below to find out more")
    print(f" A. Monte Cristo \n B. Ruben \n C. Submarine \n D. Grilled Cheese \n E. Gyro")
    letter = str(input("Please enter the letter of your choice:"))

    if letter.lower == MC:
        a()
    elif letter.lower() == R:
        b()
    elif letter.lower() == S:
        c()
    elif letter.lower() == GC:
        d()
    elif letter.lower() == G:
        e()
    else:
        print("Error accored please try again")
        main()


def a():
    print("Fresh Monte Cristo")
    print("Served with a side of hot tomato soup.")


def b():
    print("Fresh Rubem")
    print("Served with a side of hot tomato soup.")


def c():
    print("Submarine")
    print("Served with a side of hot tomato soup.")


def d():
    print("Grilled Cheese")
    print("Served with a side of hot tomato soup.")


def e():
    print("Gyro")
    print("Served with a side of hot tomato soup.")


main()
