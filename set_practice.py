



# populate "squares" with the set of all of the integers less
# than 2000 that are square numbers


# Note: If you want to call the nearest_square function, you must define
# the function on a line before you call it. Feel free to move this code up!
def nearest_square(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2


squares = set()
x = 1
while x**2 < 2000:
    squares.add(x**2)
    x += 1

print(squares)