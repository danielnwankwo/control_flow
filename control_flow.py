# control flow
# if statements
# syntax: if then conditions

age = 15
# will run because conditions have been met. without the = then it will not run as 15 does not satisfy either statement
# by itself
if age > 15:
    print("Thank You. You may watch this movie ")

elif age <= 15:
    print("sorry you are not the required age to watch this movie ")

else:
    print("oops something has gone wrong, please try again later ")


# create program using control flow with if, elif and else
# using operators == >=
# check age restrictions before selling tickets
# U, PG, 12, 15, 18
# else block should ensure to display message if other conditions do not match

age = 21

if age >=  4:
    print("Thank you, you may watch U rated movie")

elif age >= 10:
    print(" Thank you, you watch the PG movie but you will need a guardian")

elif age >= 12:
    print("thank you, you may watch this 12 rated movie")

elif age >= 15:
    print("thank you, you may watch this 15 rated movie")

elif age >= 18:
    print("Thank you, you may watch this 18 rated movie")

else:
    print("oops something has gone wrong, please try again")

# too messy, shorted later