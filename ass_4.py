# Here’s a sample Input array for questions 6 & 7: 
# [3, 'a', 'a', 'a', 2, 3, 'a', 3, 'a', 2, 4, 9, 3];
# Write a JavaScript function to find the most frequent item of an array. Kinda Hard (Pseudocode pls)
# Write a JavaScript function to remove duplicate items from an array. Kinda Hard (Pseudocode pls)

# to check for the most occuring item in a list, i will create a dictionary of the distinct elements in the list and increment the 
# count by 1 for every time it occurs in the list
        
# define the array array_mode that accepts arg num_list
def array_mode(num_list):
    # create an empty dictionary
    new_dict = {}
    # write a for loop to that checks each element in the array 
    for num in num_list:
        # if element is existent in the dictionary is existent in dictionary increment value by 1 
        if num in new_dict.keys():
            new_dict[num] += 1
        #else set value to 1  
        else:
            new_dict[num] = 1
    # find the max value in the dictionary & prints it corresponding key 
    return max(new_dict, key=new_dict.get)
test = [3, 'a', 'a', 'a', 2, 3, 'a', 3, 'a', 2, 4, 9, 3]
print (array_mode(test))

def duplicate_remover(num_list):
    new_list = list(set(num_list))
    return new_list

print(duplicate_remover(test))

# Given the array color = ["Blue ", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow "];
# Write a JavaScript function to print to console the colors in the following way:
# "1st choice is Blue ."
# "2nd choice is Green."
# "3rd choice is Red."
# ....
#define function that accepts lists 
def colour_choices (colour_list):
    # create iterbale that return ordinal numbers e.g 1st,2nd,3rd,4th etc
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
    # define variable list_counter that counts  number of elements in the list arguement
    list_counter = 1
    # define variable that will be used as an index for the list arguement in 
    # the while loop below, the index will be used to return actual values in the list 
    list_index_variable = 0
    #whileloop checks the length of the colour_list arguement in order that the ordinal values 
    #do not fall out of range with elements in the colour_list arguement 
    while list_counter <= len(colour_list):
        # print the required output
        print (" {} choice is {} ".format(ordinal(list_counter),colour_list[list_index_variable]))
        # increment list counter by 1
        list_counter +=1
        # increment index_variable by 1
        list_index_variable +=1
# test with array
test = ["Blue ", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow "]
# print function with test array
colour_choices(test)

# There are two arrays with individual values, write a JavaScript function to compute the sum of each individual index value from the given arrays.
# Sample array :
# array1 = [1,0,2,3,4]
# array2 = [3,5,6,7,8,13]
# Expected Output :
# [4, 5, 8, 10, 12, 13]
# define a function that accepts two arrays as an arguement
def list_addition(list_1,list_2):
    # return zip(list_1,list_2)
    # create a list where the results will be appended to
    new_list = []
    # write a for loop that iterates the two list arguements (list_1 and list_2)
    for l,n in zip(list_1,list_2):
        # add each corresponding element between both list arguements and append to the 
        # list created earlier
        new_list.append(l+n)
    # if the length of first list is greater than length of second list 
    if len(list_1) < len(list_2):
        # add the extra elements in the list to the new_list []
        new_list = new_list + ((array2[len(array1):]))
    # else length of second list is greater than length of first list
    else:
        # add the extra elements in the list to the new_list []
        new_list = new_list + ((array1[len(array2):]))
    # return the final version of new_list
    return (new_list)


array1 = [1,0,2,3,4]
array2 = [3,5,6,7,8,13]

print(list_addition(array1,array2))