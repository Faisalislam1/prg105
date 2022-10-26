

print("This program will total and average numbers in your data file.")
s = input("Enter the name of your file:")
counter = 1
total = 0.0
try:
    data = open(s, 'r')
except FileNotFoundError:
    print(f"Unable to access the file: {s}")

else:

    for line in data:

        line = line.strip('\n')
        try:
            num = float(line)
            print(f'{num:,.2f}')
            total += float(num)
            counter += 1
        except ValueError:

            print(f"Line {counter} with a value of {line} was invalid")
            counter -= 1
    print(f"Total {total:,.2f}")
    print("Number of entries:", counter)
    print(f"Average: {total/counter:,.2f}")

