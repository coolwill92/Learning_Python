#Conditional statements are used if we need a program that may have branching paths

# IF STATEMENTS
# These are blocks of code that will run if a certain condition is met

isWillcool = False
if isWillcool:
    print("Will is cool")
else:
    print("Will is not cool")


#-----------------------------------------------

#The OPERATORS we can use

# == Equal to
# != Not Equal to
# < Less than
# > Greater than
# <= Less than or equal to
# >= Greater than or  equal to

#The LOGICAL OPERATORS we can use

# and
# or
# not


#-----------------------------------------------

# ELSE IF together make ELIF
# Rememebr if we do IF, ELIF, ELIF we have to finish on ELSE

score = int(input("Enter your Score: "))

if score >= 85:
    print("Dictinction")
elif score >= 65:
    print("Pass")
else:
    print("Fail")
