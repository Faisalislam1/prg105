"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""

# TODO 6.1 Introduction to File Input and Output
print("=" * 10, "Section 6.1 file input and output", "=" * 10)
# 1) Assign the variable file_variable to open states.txt in read mode
file_states = open('states.txt', 'r')

# 2) Close the file
file_states.close()

# 3) Assign the variable state_capitals to open capitals.txt in write mode.
#    Please note, the file does not currently exist, and by opening it in
#    write mode you will create it
state_capital = open('capital.txt', 'w')

# 4) Write three state capitals to the file with each capital and state pair on a separate line
#    There is a list of state capitals here: https://en.wikipedia.org/wiki/List_of_capitals_in_the_United_States
# Sample:
#   state_capitals.write("Alabama, Montgomery\n") - make sure to include the \n as a new line symbol
state_capital.write('Illinois, Springfield\n')
state_capital.write('Maryland, Washington D.C\n')
state_capital.write('Alabama, Montgomery\n')
# 5) Close the file
state_capital.close()

# TODO 6.1 reading data in from a file
print("=" * 10, "Section 6.1 reading data from a file", "=" * 10)
# 1) Assign the variable states_data to open states.txt in read mode
state_data = open('states.txt', 'r')
# 2) Read in three lines from the file, assign one line to each variable below, Remove """   """ to test

line1 = state_data.readline()
line2 = state_data.readline()
line3 = state_data.readline()

 
# 3) Close the file
state_data.close()
# 4) Print the three variables
print(line1)
print(line2)
print(line3)

# TODO 6.2 Using loops to process files
print("=" * 10, "Section 6.2 use loops to process files", "=" * 10)
# Complete the program below to Read in and Count all entries in the states file
# Remove the """ """ before testing
# 1) Open the file in read mode using states_file as the file variable

states_file = open('states.txt', 'r')

counter = 0
for line in states_file:
    line = states_file.readline()
    print(line)
    counter = counter+1

print(counter)
# 2) Write a for loop to read in all of the lines,
# -- print each line on the screen,
# -- also add 1 to counter for each line

# 3) Close the file
states_file.close()
# TODO 6.3 Processing records
print("=" * 10, "Section 6.3 processing records", "=" * 10)
# You are going to finish the program below to write book information to a file
books = 3      # use this as the number of books to enter

# 1) open the file books.txt for writing, using the variable books_file
# Remove the """ """ to test
books_file = open('books', 'w')

# 2) Use a for loop to get a title and author from the user using a range of 1, books + 1
# -- get the data from the user in the loop
# -- write the data to the file as a record while in the loop,
#    make sure to include the \n at the end of the line

for books in range(1,books+1):
    word = input(("Please enter a the title of the bookand name of the author\n"))
    books_file.write(word)
    books_file.write("\n")

# 3) Close the file
books_file.close()
# TODO 6.4 Exceptions
print("=" * 10, "Section 6.4 exceptions", "=" * 10)
# In this exercise you will try to open a file that does not exist,
# capture the error, and display a custom error message

# 1) Create a try statement
try:
    superhero = open("superheros.txt", "r")

except FileNotFoundError:
    superhero = open("superheros.txt", "w")
    superhero.close()
    print("File Created")
except IOError:
    print("File doesn't exist")

# 2) Open the file superheros.txt for READING (we are not writing, it would create the file)

# 3) Close the file

# 4) Create an except IOError, that uses a print statement to tell the user that the file doesn't exist
