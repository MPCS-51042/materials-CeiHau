
def mean(string_of_numbers):
    '''
        This function takes in a space-separated string of integers and floats and
        returns a their mean as a float.

        Inputs:
            string_of_numbers (string): a space-separated string of integers and floats.

        Output:
            a float, the mean of the inputted numbers.
        '''
    lst = string_of_numbers.split()
    lst = list(map(int,lst))
    if(len(lst) == 0):
        return 0
    else:
        return sum(lst)/len(lst)