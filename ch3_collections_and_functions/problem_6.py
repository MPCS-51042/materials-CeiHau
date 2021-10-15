from problem_4 import taxes_owed


def inflection_point():
    '''
        This function returns a float representing the income at which
        Townsville's graduated income tax would be higher than a flat
        5% income tax.
    '''
    income = 1
    graduated_tax = taxes_owed(income)
    flat_tax = income * 0.05
    while graduated_tax < flat_tax:
        income = income + 1
        graduated_tax = taxes_owed(income)
        flat_tax = income * 0.05
    return float(income)


