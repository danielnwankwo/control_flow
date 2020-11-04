# this lesson will cover control flow
## if statements, elif and else statements
### for loops and while loops 

- for loops are used to iterate through data
- syntax for ```variable_name in name_of_data_collection_variable``

```shopping_list = ["eggs", "milk", "supermalt"]
print(shopping_list)``

# for items in shopping_list:
   
   `` if items == "milk":
        print(items)
         break``

    ``for items in shopping_list:
        if items == "milk":
            print(items)
            continue``


# task 1 loop print hello 10 times
for num in range(10):
    print("Hello")

# Task 2 - Create another loop with a range that asks for names and appends to list_names
# Creating an empty list that we can add to
``names_list = []
# Loop 10 times as
for _ in range(10):
    name = input("Please enter a name:  ")  # user input and assigning the name variable
# Adding the name given to the list
    names_list.append(name)
# Printing the list
print(names_list)``

# Task 3 - Make a loop that iterates over each name in list_name and format's it into lowercase in a new variable called list_names_lower
for names in names_list:
    ``lowercase_names_list = names.lower() # Converts all the names back into lower case and stores in a new variable
    print(lowercase_names_list)``


# Python program to print odd Numbers in given range
``start, end = 0, 10``

# iterating each number in list (start, end +1)
``for num in range(0, 11):

    if num % 2 != 0:
        print(num, "odd")

    elif num % 2 == 0:
        print(num, "even")``

- while loops are not regularly used however when they are, it is usually for monitoring
- we have keywords ```break``` and ``continue`` that help control the flow of our loop

 ``` number = 0

 while number < 10:
     print(f"it is working -> {number}")
     if number == 4:
         break
     number += 1 ``` 

# take user input with while loop

user_prompt = True

``while user_prompt:
    # this user input is within the while loop and will keep prompting the user till we get the age in digits
    age = input("Please enter your age ")
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("Please provide age in digits")
    print(f"your age is {age}")```

# isdigit() checks if input is all digits
