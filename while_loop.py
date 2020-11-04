# while loop
# break and continue are keywords that we can use to control the flow of our program
# syntax: while variable_name condition value:
# COPY OVER TASKS FOR IF STATEMENTS AND FOR LOOPS WITH PSEUDO THEN THROW TO GITHUB

#
# number = 0
#
# while number < 10:
#     print(f"it is working -> {number}")
#     if number == 4:
#         break
#     number += 1

# take user input with while loop

user_prompt = True

while user_prompt:
    # this user input is within the while loop and will keep prompting the user till we get the age in digits
    age = input("Please enter your age ")
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("Please provide age in digits")
    print(f"your age is {age}")

# isdigit() checks if input is all digits
