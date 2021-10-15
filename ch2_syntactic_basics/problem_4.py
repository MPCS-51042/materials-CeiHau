def expand_letter_ranges(string_of_letters):
    '''
        This function takes in a comma-separated string of letters and letter ranges and
        returns a list of the letters and expanded ranges in alphabetical order.

        Inputs:
            string_of_letters (string): a comma-separated string of letters and letter ranges.

        Output:
            a list of the letters and expanded ranges in alphabetical order.
        '''
    string_of_letters = string_of_letters.replace(' ', '')
    string_of_letters = string_of_letters.upper()
    lst = string_of_letters.split(',')
    result = []
    for value in lst:
        if len(value)==0:
            continue
        if len(value) == 1:
            if value not in result:
                result.append(value)
        else:
            for asc in range(ord(value[0]), ord(value[2]) + 1):
                if chr(asc) not in result:
                    result.append(chr(asc))
    result.sort()
    return result

