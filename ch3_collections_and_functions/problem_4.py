def taxes_owed(income):
    '''
        This function takes in an income as an integer or float and
        returns taxes owed as a float, truncated at two digits.

        Inputs:
            income (integer or float)

        Output:
            taxes owed (float)
        '''
    if income <= 40000:
        return 0
    elif 40000 <= income <= 60000:
        return (income - 40000) * 0.02
    elif 60000 <= income <= 90000:
        return 20000 * 0.02 + (income - 60000) * 0.05
    elif 90000 <= income <= 120000:
        return 20000 * 0.02 + 30000 * 0.05 + (income - 90000) * 0.07
    elif 120000 <= income <= 150000:
        return 20000 * 0.02 + 30000 * 0.05 + 30000 * 0.07 + (income - 120000) * 0.09
    elif 150000 <= income <= 180000:
        return 20000 * 0.02 + 30000 * 0.05 + 30000 * 0.07 + 30000 * 0.09 + (income - 150000) * 0.11
    elif 180000 <= income <= 210000:
        return 20000 * 0.02 + 30000 * 0.05 + 30000 * 0.07 + 30000 * 0.09 + 30000 * 0.11 + (income - 180000) * 0.13
    elif 210000 <= income <= 240000:
        return 20000 * 0.02 + 30000 * 0.05 + 30000 * 0.07 + 30000 * 0.09 + 30000 * 0.11 + 30000 * 0.13 + (
                income - 210000) * 0.15
    elif 240000 <= income:
        return 20000 * 0.02 + 30000 * 0.05 + 30000 * 0.07 + 30000 * 0.09 + 30000 * 0.11 + 30000 * 0.13 + 30000 * 0.15 + (
                    income - 240000) * 0.2
    return income

# print(taxes_owed(40000))
# print(taxes_owed(100000))
# print(taxes_owed(187000))
# print(taxes_owed(238000))
# print(taxes_owed(1000000))
#
#
#
#
# x = 2
# print(3 <= x <= 3)

#10min