
# task 1 loop print hello 10 times
for num in range(10):
    print("Hello")

# Task 2 - Create another loop with a range that asks for names and appends to list_names
# Creating an empty list that we can add to
names_list = []
# Loop 10 times as
for _ in range(10):
    name = input("Please enter a name:  ")  # user input and assigning the name variable
# Adding the name given to the list
    names_list.append(name)
# Printing the list
print(names_list)

# Task 3 - Make a loop that iterates over each name in list_name and format's it into lowercase in a new variable called list_names_lower
for names in names_list:
    lowercase_names_list = names.lower() # Converts all the names back into lower case and stores in a new variable
    print(lowercase_names_list)


# Python program to print odd Numbers in given range
start, end = 0, 10

# iterating each number in list (start, end +1)
for num in range(0, 11):

    if num % 2 != 0:
        print(num, "odd")

    elif num % 2 == 0:
        print(num, "even")




