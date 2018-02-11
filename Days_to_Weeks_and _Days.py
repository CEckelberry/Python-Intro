def readable_timedelta(days):
    """Function takes the number of days and returns weeks+day(s)"""
    delta_days = (days % 7)
    delta_weeks = int(days / 7)
    return ("{} week(s) and {} day(s)".format(delta_weeks, delta_days))


# Uncomment this function call to test it:
print(readable_timedelta(9))
print(readable_timedelta(105))
print(readable_timedelta(0))
print(readable_timedelta(1))
print(readable_timedelta(6))
print(readable_timedelta(9912))