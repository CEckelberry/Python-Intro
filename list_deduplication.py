def remove_duplicates(entry_list):
    """
    This function will add any unique elements in a list (no repeating members) and store them in a new list.
    :param Entry_list lists of any size with strings or numbers:
    :return: Deduplicated list
    """
    comparison_list = []
    for x in entry_list:
        if x not in comparison_list:
            comparison_list.append(x)

    return comparison_list
print(remove_duplicates(['Angola', 'Maldives', 'India', 'United States', 'India']))