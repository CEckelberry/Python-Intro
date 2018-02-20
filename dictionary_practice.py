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


"""
def most_prolific(practice_input):

    temp_list = []
    year_list = {}
    max_years = []
    max_number = 0
    years = {}

#Store the years in a dictionary and then the total # of albums released per year
    for years in practice_input:
        year = practice_input[years]
        if year in year_list:
            years[year] += 1
        else:
            years[year] = 1

    for year in years:
        if year_list[year] > max_number:
            max_years.append(year)
            max_number = year_list[year]
        elif year_list[year] == max_number and not (year in max_years):
            max_years.append[year]
    if (len(max_years == 1)):
        return max_years[0]
    else:
        return max_years




print(most_prolific(Beatles_Discography))

"""


monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}







def total_takings(monthly_input):
    for z in monthly_input:
        turns = 0
        total_array = []
        final_array = []
        while turns < len(monthly_input):

            #print(len(monthly_input))
            total_array = total_array.append(print(monthly_input.values()))
            print("You are in the loop")
            turns += 1
            return final_array, total_array






print(total_takings(monthly_takings))

