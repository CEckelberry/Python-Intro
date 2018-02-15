def list_sum(input_list):
    input_sum = 0
    # Write a for loop that adds the elements
    # of input_list to the sum variable
    for inputs in input_list:
        input_sum += inputs
    return input_sum



#These test cases check that list_sum works correctly
test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))




"""Write a function, `tag_count`, that takes as its argument a list
of strings. It should return a count of how many of those strings
are XML tags. You can tell if a string is an XML tag if it begins
with a left angle bracket "<" and ends with a right angle bracket ">".
"""
# Define the tag_count function
def tag_count(list_input):
    temp_count = 0
    for x in list_input:
        if x[0] == "<" and x[-1] == ">":
            temp_count += 1
    return temp_count


# Test for the tag_count function:
list1 = ['<greeting>', 'Hello World!', '</greeting>']
total_count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(total_count))


def html_list(html_input):
    statement = ("<ul>")
    for x in (html_input):
        #add list statements onto both sides of the input string\list
        statement += "\n" "<li>" + str(x) + "</li>"
        #adds the to statement
    statement += "\n" +"</ul>"
    return statement

print(html_list(["first string","second string"]))
print(html_list([1, 2, 3]))


print(html_list(["strings", 2.0, True, "and other types too!"]))





def starbox(width, height):
    """print a box made up of asterisks.

    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    """
    print("*" * width) #print top edge of box

    # print sides of box
    for _ in range(height-2):
        print("*" + " " * (width-2) + "*")

    print("*" * width) #print bottom edge of box


# Test Cases
print("Test 1:")
starbox(5, 5)  # this prints correctly

print("Test 2:")
starbox(2, 3)  # this currently prints two lines too tall - fix it!




