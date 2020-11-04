from datetime import date

# for defining age and name of user
name = input("What is your name ")
age = int(input("how old are you "))

# if they have already had their birthday
birth_date_ask = input("Have you had your birthday yet this year  (y/n) ")

# if answer is yes then print age from this year
if birth_date_ask.lower() == 'y':
    birth_year = int(date.today().year) - age

# to account if they have not had their birhtday yet
else:
    birth_year = int(date.today().year) - (age + 1)


print(f"OMG {name} you are {age} years old and you were born in {birth_year}.")
