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


Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}



def most_prolific(discs):
#We will store a dictionary of years
#and number of albums per year
    years = {}
    maxyears = []
    maxnumber = 0
    for disc in discs:
        year = discs[disc]
        if year in years:
            years[year] += 1
        else:
            years[year] = 1

#find the year in which the maximum
#number of albums was published
#there are more elegant ways of accomplishing this,
#but the code below works
    for year in years:
        if years[year] > maxnumber:
            maxyears=[]
            maxyears.append(year)
            maxnumber = years[year]
        elif years[year] == maxnumber and not (year in maxyears):
            maxyears.append(year)
    if (len(maxyears) == 1):
        return maxyears[0]
    else:
        return maxyears


print(most_prolific(Beatles_Discography))




monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}



def total_takings(monthly_takings):
    #total is used to sum up the monthly takings
    total = 0
    for month in monthly_takings.keys():
        #I use the Python function sum to sum up over
        #all the elements in a list
        total = total + sum(monthly_takings[month])
    return total


print(total_takings(monthly_takings))








