print("PLAY PRICES PER TICKET")
print("1. Student $5.00")
print("2. Veteran $7.00")
print("3. Show Sponsor $2.00")
print("4. Retiree $6.00")
print("5. General Public $10.00")
per = float(0)
c = float(0)
m = float(10)
p = float(input("Please enter the number of the category you fir for purchasing tickets:", ))
v = float(input("How many tickets would you like to buy ", ))
if p == 1:
    c = 5
elif p == 2:
    c = 7
elif p == 3:
    c = 2
elif p == 4:
    c = 6
elif p == 5:
    c = 10
if 4 <= v <= 8:
    per = .9
elif 9 <= v <= 15:
    per = .85
elif v > 15:
    per = .8
cost = float(c * v)
discount = float(per * c)
o = float(discount * v)
q = float(discount / v)

print(f"Cost before any discounts were applied:${cost:.2f}")
print(f"Your cost after all discounts were applied ${o:.2f}")
print(f"Your price is ${discount:.2f} per ticket")
