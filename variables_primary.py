# author: Lynijah Russell
# date: 07-02-2021
#
# description: variables 

# --------------- Section 1 --------------- #
def blank():
    return print(" ")
# 1.1 | Variable Creation | Strings
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# Variables
#   1) Create a variable that holds your name.
#   2) Create a variable that holds your birthday.
#   3) Create a variable that holds the name of an animal you like.
#
# Print
#   4) Print each variable, describing it when you print it.
#
# Example Code

# WRITE CODE BELOW
name= "Lynijah Faith Russell"
birthday="January 13th 2006."
animal= "are cats "

print("My name is", name, "but my friends call me Cupid or Faith")
blank()
print("My birthday is", birthday, "yes, I was born on Friday the 13th, dont judge me lol")
blank()
print(" My favorite animals", animal)
blank()
# 1.2 | Variable Creation | Integers / Floats
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# All variables created in this section should hold either an integer or float.
#
# Variables
#   1) Create a variable that holds your favorite number.
#   2) Create a variable that holds the day of the month of your birthday.
#   3) Create a variable that holds a negative number.
#   4) Create a variable that holds a floating (decimal) point number.
#
# Print
#   5) Print each variable, describing the value you print.

# WRITE CODE BELOW
favNum= 13
bdayNum= 13
negNum= -13
floatNum= 13.13
blank()
print("This is my favorite number:", favNum)
blank()
print("This is the day of my birthday month that I was born on:", bdayNum)
blank()
print("This is a negative number:", negNum)
blank()
print("This is a float:", floatNum)
blank()


# 1.3 | Overwriting Variables
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# Variables
#   1) Overwrite the variable holding your name, and save a different name to it.
#   2) Overwrite the variable holding birthday with the day you think would be best to have a birthday on.
#   3) Overwrite the variable holding your favorite number and set it to a number you think is unlucky.
#
# Print
#   4) Print the variables you've overwritten, describing the values you print.
#
# Example Code
# example_name = 'lucia'
# print('EXAMPLE: my new name is', example_name)

# WRITE CODE BELOW
name= "Cupid"
bdayNum= 33
favNum= 11
blank()
print("My nickname is:" , name )
blank()
print("The day I should have been born is:", bdayNum)
blank()
print("Unlucky day in my opinion is", favNum)
blank()


# 1.4 | Operations
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# Variables
#   1) Create a variable that is the sum of two numbers.
#   2) Create a variable that is the product of three numbers.
#   3) Create a variable by dividing the previously created sum, with the previously created product.
#
#   4) Create a variable that is the concatenation of your name and an animal you like (use the variables!)
#   5) Create a variable that is an acronym (like 'lol') multiplied by your birth day.
#
#   6) Create a variable that is difference of itself minus the number you think is unlucky.
#   7) Overwrite the lucky variable with the itself squared.
#
# Print
#   7) Print all the new variables you've created along with what the represent
#
# Example Code
# example_sum = 11 + 21
# print('EXAMPLE: the sum of 11 and 21 is', example_sum)

# WRITE CODE BELOW
sum1= 200+219
product1= 2*8*6
division= sum1/product1
nameAnimal= name + animal
acronym= "LMA"*1 + "O"*13
num1= 3
num1-= favNum
favNumSquared= favNum**2

blank()
print("This is the sum of two numbers", sum1)
blank()
print("This is the products of three numbers", product1)
blank()
print("This is the division of ", sum1, "/", product1, "." , division)
blank()
print("This is string concatenation between my name and fav animal" , nameAnimal)
blank()
print("The acronym i made is", acronym)
blank()
print("This is a number - itself and my unlucky number", num1)
blank()
print("This is my now unlucky number squared", favNumSquared)