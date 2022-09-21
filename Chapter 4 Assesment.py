

age = float(input("How old are you currently?", ))
retire = float(input("What age do you want retire?",))
income = float(input("What is your yearly income?"))
save = float(input("What percent of your income do you save"))
saved = float(input("How much money do you have saved"))
print("This Projection assumes a 3% raise wach year and a 6% yearly return on investment.")
y = 1
save = (save*.01)
contribution = income*save
print("Year               Income             Savings Contribution           Total Savings")
while age < retire:
    saved += saved * .06
    saved += contribution
    print(f" {y:2d}{income:21,.0f}{contribution:25,.0f}{saved:29,.0f}")
    age += 1
    y += 1
    income = income +(income*.03)
    contribution = income*save



