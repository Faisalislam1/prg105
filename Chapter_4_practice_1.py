

total_sales = 0
weekly_sales = 0
for date in ['Monday', 'Tuesday', 'Wednesday', 'Thurday', 'Friday', 'Saturday', 'Sunday']:

    total_sales = int(input(f"what are the sales on {date}:"))
    weekly_sales += total_sales

print(f"The total amount of sales for the week was: $ {weekly_sales:,.2f}")
print(f"The average amount of sales per day was: $ {weekly_sales/7:,.2f}")
