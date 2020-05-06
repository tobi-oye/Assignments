# Fifth assignment:
# Create a function that takes in an array of numbers. The function should multiply all elements of the array by 2 and return the modified array
def array_multiplier_2 ( elements = []):
    new_array = [element * 2 for element in elements]
    return new_array
# Sixth assignment:
# Create a function that takes in 2 arguments. The first argument is an array and the second argument takes in a value. The function should push whatever value from the 2nd arguments into the array and return the modified array

def append_second_arguement (elements,y):
    elements.append(y)
    return elements
# Seventh assignment: (V. Hard)
# First create an array of objects called data with the following values:

# 1. Principal- 2500, time- 1.8
# 2. Principal- 1000, time- 5
# 3. Principal- 3000, time- 1
# 4. Principal- 2000, time- 3

# NB: Each individual object should have 'principal' and 'time' as keys.
# Write a function called "interestCalculator" that takes an array as a single argument and does the following:

# Determine the rate applicable using the conditions:
# * If the principal is greater than or equal to 2500 and the time is greater than 1 and less than 3, then rate = 3
# * If the principal is greater than or equal to 2500 and the time is greater than or equal to 3, then rate = 4
# * If the principal is less than 2500 or the time is less than or equal to 1, then rate = 2
# * Otherwise, rate = 1;

# Calculate the interest for each individual object using the formula: (principal * rate * time) / 100. 
# The function should return an array of objects called 'interestData' and each individual object should have 'principal', 'rate', 'time' and 'interest' as keys with their corresponding values.
# Log the 'interestData' array to console BEFORE your return statement.
# Finally, call/execute the function and pass the 'data' array you created.

# create an array of objects that have key value pairs 
data = [{'principal': 2500, 'time':1.8},{'principal': 1500, 'time':5},{'principal':3000, 'time':1},\
    {'principal': 2000, 'time':3}]
# create a function that takes an array as an argument
def interestCalculator(elements = []):
    interest_data = []
    # iterate through the elements in the list in order to get the values of principal and time
    i = 0 
    for element in elements:
        # * If the principal is greater than or equal to 2500 and the time is greater than 1 and less than 3, then rate = 3
        if element['principal'] >= 2500 and element['time'] > 1 and element['time'] < 3:
            # set the rate equal to 3 
            rate = 3
        # * If the principal is greater than or equal to 2500 and the time is greater than or equal to 3, then rate = 4
        elif element['principal'] >= 2500 and element['time'] >= 3 :  
            rate = 4
        # * If the principal is less than 2500 or the time is less than or equal to 1, then rate = 2
        elif element['principal'] < 2500 and element['time'] <= 1 :
            rate = 2
        # * Otherwise, rate = 1;
        else:
            rate = 1 
        interest = (element['principal'] * rate * element['time'])/100

        interest_data.append({'principal':element['principal'],'time':element['time'],'interest':interest})
       
    return interest_data

interestCalculator(data)
