def convert_to_0_if_None(unit, dictionary):
    if unit in dictionary:
        return str(int(dictionary[unit]))
    else:
        return "0"