def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    # TODO: implement this function
    if len(input_list) < 3:
        return sorted(input_list, reverse=True)
    else:
        sl = sorted(input_list)
        return sorted((sl[-3:]), reverse=True)


print(top_three([2, 3, 5, 6, 8, 4, 2, 1]))