gpa = 0.00
felony = "y"
credit = 0
income = 100000
student = input("Are you a new or returning student Please enter n or r: ", )
gpa = float(input("Whats your gpa", ))
felony = input("Have you been convicted of a drug felony Please enter y or n: ", )
credit = int(input("How many credit hours are you enrolled for the semester?", ))
income = int(input("what is your yearly income rounded to the nearest dollar", ))

if not felony == "n" or credit >= 6 or income <= 50000 or gpa >= 2.0:
    print("You are not eligible")
if felony == "n" and credit >= 6 and income <= 50000 and gpa >= 2.0:
    print("You are eligible")
