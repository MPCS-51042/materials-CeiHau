def find_twos(string_1, string_2):
    '''
        This function takes in two strings that only contains integers, commas and whitespace and
        returns a list of integers, where each integer,

           1. Appears in both strings
           2. Contains a 2 as a digit in the number.

        Inputs:
            str1, str2 (string): strings that contains integers, commas, and whitespace. You can assume each integer is separated by a single comma followed by zero or more whitespaces.

        Output:
            A list of integers, where the list contents is described by above. The returned list must not contain duplicates.
        '''

    string_1 = string_1.replace(' ','')
    string_2     = string_2.replace(' ','')
    lst_1 = string_1.split(',')
    lst_2 = string_2.split(',')

    result = []
    for index_1, value_1 in enumerate(lst_1):
        if '2' in value_1:
            for index_2, value_2 in enumerate(lst_2):
                if value_1 == value_2 and value_1 not in result:
                    result.append(value_1)
    result = list(map(int, result))
    return result