def words(a_string):
    """
    This function accepts a string as an argument and
    returns a dictionary of each word in the string along with
    the number of its occurances.
    """
    string_list = a_string.split()
    string_dict = {}
    
    for item in string_list:
        if item.isdigit():
            # Convert the key to an integer if it is a digit.
            string_dict[int(item)] = string_list.count(item)
        else:
            string_dict[item] = string_list.count(item)
    return string_dict