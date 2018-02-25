def hours2days(hour_input):
    return int((hour_input / 24)), int((hour_input % 24))


print(hours2days(24))
print(hours2days(10000))