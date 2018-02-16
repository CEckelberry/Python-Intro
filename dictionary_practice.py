# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {"Shanghai":17.8, "Istanbul":13.3, "Karachi":13.0, "Mumbai":12.5}

print(population["Shanghai"])

#print(population["Texas"])



from countries import country_list # Note: since the list is so large, it's tidier
                                   # to put in in a separate file. We'll learn more
                                   # about "import" later on.

country_counts = {}
###for loop to process country_list
for country in country_list:
    x = 0
    #loop to run through the list while x is less than the length of country_list
    while x < len(country_list):
        #does not count the list if it already exists in country counts dictionary
        if country in country_counts:
            None
            x += 1
        #adds the key value to the dictionary and the key pair which is the # of times the string existed in the list
        else:
            country_counts.update({str(country): country_list.count(str(country))})
            x += 1


print(country_counts)

    # If the country isn't in the dict already, add it and set the value to 1
    # If the country is in the dict, increment its value by one to keep count