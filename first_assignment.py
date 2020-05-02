# First assignment:
# Create a function that takes in 2 arguments which are numbers. 
# If the first argument is greater than the 2nd, it should return a string 'First number is greater than second number'. 
# Else if the second argument is greater than the 1st, it should return a string 'Second number is greater than the first number'. 
# Else it should return a string 'The numbers are the same'

#solution 
# assumptions input is two integer numbers , output is a string a describing relationship between the numbers
#define a function number_rel with arguements value_1 and value_2
def number_rel(value_1,value_2):
    # Ensure the inout values are integers
    if isinstance(value_1,int) and isinstance(value_2,int) :
        # if the value_1 is greater than value_2
        if value_1 > value_2:
            # return value_1 is greater than value_2
            return "First number:{} is greater than Second number {}".format(value_1,value_2)
        # if the value_1 is less than value_2 
        elif value_1 < value_2:
            # return value_2 is greater than value_1
            return "Second number: {} is greater than First number {}".format(value_2,value_1)
        # else 
        else:
            # return the numbers are the same
            return "The numbers are the same"
    #otherwise arguements only accepts integer values
    else:
        return "accepts only integer values"

# Second assignment:
# Create a function that takes in 2 arguments. 
# The first argument is the name and 2nd argument is the age. 
# This function should return a string that interpolates the 2 arguments in such a way 'The name of the user is _ and their age is __'
# e.g. Arguments are Shehu and 23. Result: The name of the user is Shehu and their age is 23

#solution 2 
#assumptions input is name and age, output is a string that gives info of the name and the age
# define a function name_age_info with arguements name and age 
def name_age_info (name,age):

    #Ensure the value of age is an integer
    if isinstance(age,int):
        # return the name and age of the was parsed in 
        return "The name of the user is {} and their age is {}".format(name,age)
    #otherwise state the second arguement accepts strings only
    else:
        return "second arguement accepts only integers"

# Third assignment:
# Create a function that takes in 1 argument which is a string. 
# If the string length is greater than or equal to 5, return the string 'This word is long'. 
# If the string length is lesser than 5, return the string 'This word is short'

#solution 
# assumptions input is a string , output is a string detailing the string length
#define a function string_info with inputs value
def string_info(value):
    # Ensure the input is a string 
    if isinstance(value,int):
        # if length of string is greater than or equal to five
        if len(value) <= 5: 
            # return a string that says the "the word is short"
            return 'This word is long'
        # otherwise
        else:
        #     retun a string that says "the word is short"
            return 'This word is short'
    # if the input is not a string
    else:
        return "input is a string, but arguement requires int values"
# Fourth assignment:
# Create a function that takes in 3 arguments. The function should return an addition of all 3 numbers

#solution
#assumptions input is 3 numbers  and output is the sum of the three 3 numbers

# define a fucntion sum_of_numbers that accepts three values ---> value_1, value_2 and value_3
def sum_of_numbers(value_1,value_2,value_3):
#ensure the arguement accepts only integers
    if isinstance(value_1,int) and isinstance(value_2,int) and isinstance(value_3,int):
        #     return the sum of the three numbers 
        sum = value_1+value_2+value_3
        return sum
    # Otherwise return to user values are not integers
    else:
        return "the values are not integers"


