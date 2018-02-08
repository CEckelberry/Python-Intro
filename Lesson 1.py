
######Part 2 Arithmetic######

print(3 +1)

print("Hello World!")

print ((1 + 2 + 3) *3)

print(3**2)

print(9 % 2)


######Part 5 Variables 1######

manila_pop = 1780148

print(manila_pop)

manila_area = 16.56

manila_pop_density = manila_pop / manila_area

print(manila_pop_density)

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8

# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall = rainfall - (rainfall*.10)

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
reservoir_volume = reservoir_volume + (reservoir_volume * .05)
# into the reservoir in the days following the storm

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume = reservoir_volume - (reservoir_volume * .05)
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable
print(reservoir_volume)



######Part 10 Types and Conversions######


print(type("This is a String"))

print(type(88.0))

print(type(88))



mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

number_conversion_1 = int(mon_sales)
number_conversion_2 = int(tues_sales)
number_conversion_3 = int(wed_sales)
number_conversion_4 = int(thurs_sales)
number_conversion_5 = int(fri_sales)

total_sales = (number_conversion_1 + number_conversion_2 + number_conversion_3 + number_conversion_4 + number_conversion_5)
total_sales = str(total_sales)

print("This week's total sales: " + total_sales)




######Part 11/12 Types and Conversions######


prophecy = "And there shall in that time be rumours of things going astray, and there will be a great confusion as to where things really are, and nobody will really know where lieth those little things with the sort of raffia work base, that has an attachment…at this time, a friend shall lose his friends’s hammer and the young shall not know where lieth the things possessed by their fathers that their fathers put there only just the night before around eight o’clock…"

vowel_count = 0

###set the value of vowel_count to be the number of vowels in prophecy###

vowel_count = prophecy.count("a")
vowel_count += prophecy.count("e")
vowel_count += prophecy.count("i")
vowel_count += prophecy.count("o")
vowel_count += prophecy.count("u")
vowel_count += prophecy.count("A")
vowel_count += prophecy.count("E")
vowel_count += prophecy.count("I")
vowel_count += prophecy.count("O")
vowel_count += prophecy.count("U")

# Print the final count
print(vowel_count)



test_sentence = "All around the world people need to find food in a forest"
new_sentence = test_sentence.replace("t", "q")
print("Before: " + test_sentence)
print("After: " + new_sentence)



city = "Seoul"
high_temperature = 18
low_temperature = 9
temperature_unit = "degrees Celsius"
weather_conditions = "light rain"

#rewrite this line to use the format method rather than string concatenation
alert = "Today's forecast for {}: The temperature will range from {} to {} {}. Conditions will be {}.".format(city, low_temperature, high_temperature, temperature_unit, weather_conditions)

# print the alert
print(alert)


