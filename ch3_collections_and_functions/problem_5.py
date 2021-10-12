from problem_4 import taxes_owed
import csv


def total_impact(strategy):
    '''
        This function takes in a tax strategy as a string and
        returns a tuple of tax_revenue and poverty_burden.

        Inputs:
            tax strategy (string)

        Output:
            tax_revenue and poverty_burden (tuple, float and integer)
        '''
    f = open('townsville.csv')
    csv_data = csv.reader(f)

    total_tax_revenue = 0
    poverty_num = 0
    summed_amount = 0

    if strategy == "flat_rate":
        for index, row in enumerate(csv_data):
            if index != 0:
                total_tax_revenue = total_tax_revenue + int(row[1]) * 0.05
                if int(row[1]) * 0.95 < 40000:
                    poverty_num = poverty_num + 1
                    summed_amount = summed_amount + 40000 - int(row[1]) * 0.95
    elif strategy == "graduated_rate":
        for index, row in enumerate(csv_data):
            if index != 0:
                total_tax_revenue = total_tax_revenue + taxes_owed(int(row[1]))
                if int(row[1]) < 40000:
                    poverty_num = poverty_num + 1
                    summed_amount = summed_amount + 40000 - int(row[1])

    f.close()
    return total_tax_revenue, poverty_num, float(summed_amount)


# print(total_impact("flat_rate"))
# print(total_impact("graduated_rate"))
