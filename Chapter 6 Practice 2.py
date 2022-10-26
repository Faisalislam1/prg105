

counter = 0
data = open('sales_totals.txt', 'r')
counter1 = 0
total = 0.0

for line in data:

    line = line.strip('\n')
    num = float(line)
    print(f'{num:,.2f}')
    counter += 1
    total += float(num)

print (f"Total {total:.2f}")
print ("Number of entries:",(counter))
print (f"Average: {total/counter:.2f}")


