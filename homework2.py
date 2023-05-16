def histogram(data, n, min_val, max_val):
    # data is a list
    # n is an integer
    # min_val and max_val are floats

    # Write your code here
    if min_val == max_val:  #Check to see if min and max value are the same
        print("Error: min_val and max_val are the same value")
        return []   #Return an empty list
    elif min_val > max_val: #Check to see if min value is greater than max val
        temp = max_val      #Create atemp variable to store max value so it can be later switched
        max_val = min_val   #Switch max val to the value stored in min value
        min_val = temp      #Set min val to the temp which holds the former max value
    elif n <= 0:
        return []           #Return an empty list
    else:
        hist = n * [0]      #Set histogram with n amounts spaces holding 0's
        w = (max_val - min_val) / n     #Get bin width 
        
        for value in data:      #Iterate through data list
            if value > min_val and value < max_val: #Check to see if values are within range
                temp2 = int ((value - min_val) / w) #Create a temp holding width value and set it to an int type
                hist[temp2] = hist[temp2] + 1   #Iterate through the histogram
            
    return hist
    
    



    # return the variable storing the histogram
    # Output should be a list
   

# Here, the function first checks if the lower and upper bounds are the same, 
# if they are it prints an error message and returns an empty list. 
# If lower bound is greater than upper bound, it swaps their values. 
# If number of bins is less than or equal to 0, it returns an empty list. 
# Then it initializes an empty list hist of length n and calculates the width of each bin. 
# Then it iterates through the data, 
# and for each value checks if it is within the range of the histogram and if it is, 
# it increments the bin it belongs to. Finally, it returns the histogram.

def combine_birthday_data(person_to_day, person_to_month, person_to_year):
    #person_to_day, person_to_month, person_to_year are dictionaries

    # Write your code here
                       
    
    month_to_person_data = {}         #Empty dicitonary created 
    for name in person_to_month:        #For loop creating the dictionary
        month = person_to_month[name]   #Month calcuation
        day = person_to_day[name]       #day calculation
        year = person_to_year[name]     #year calcuation
        
        age = 2022 - year            #age calculation
        
        if month in month_to_person_data.keys(): #Check the keys
            if age > month_to_person_data[month][1][2]: #Access the tuples involving age
                month_to_person_data[month] = ((name, (day, year, age)))  #replace old person with new person based on who is older
        else:
           month_to_person_data[month] = ((name, (day, year, age)))  #Keep original person or the one compared with who was already older

    return month_to_person_data
        
            
            

        
    # return the variable storing output
    # Output should be a dictionary

    

# We first define the current year as 2022, which will be used to calculate the age of each person later on.
# We create an empty dictionary month_to_person_data that will store the final data in the format specified in the problem statement.
# We iterate over the keys and values of the person_to_month dictionary using a for loop and the items() method.
# For each iteration, we extract the corresponding day, year and age values from the person_to_day and person_to_year dictionaries using the current name as the key.
# We then use the current month as the key and a tuple of (name, (day, year, age)) as the value to update the month_to_person_data dictionary.
# Finally, we return the month_to_person_data dictionary as the output of the function.