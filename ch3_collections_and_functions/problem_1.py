def calculate_metrics(filename):
    import pandas as pd
    data = pd.read_csv('metrics.csv')
    results = pd.DataFrame({"target": [], "sum": [], "count": []})
    for index, row in enumerate(data.iterrows()):
        # activity_year = {activity}({year}), e.g. Alley Grading-Unimproved(2018)
        activity_year = row[1]['Activity'] + ' (' + row[1]['Period Start'][-4:] + ')'

        # if this {activity_year} doesn't exist, add the first information of this {activity_year}
        if activity_year not in results.index:
            target = row[1]['Target Response Days']
            sum = row[1]['Average Days to Complete Activity'] * row[1]['Total Completed Requests']
            count = row[1]['Total Completed Requests']
            results.loc[activity_year] = [target, sum, count]
        # else this {activity_year} exists, change the information of it.
        else:
            target = results.loc[activity_year]['target']  # {target} should remain same
            sum = results.loc[activity_year]['sum'] + row[1]['Average Days to Complete Activity']* row[1]['Total Completed Requests']  # sum = sum + new
            count = results.loc[activity_year]['count'] +row[1]['Total Completed Requests'] # count = count + 1
            results.loc[activity_year] = [target, sum, count]
    results = results.assign(average = results['sum']/results['count'])
    solutions=[]
    for row in results.iterrows():
        activity_year = row[0]
        target = row[1]['target']
        avg = row[1]['average']
        solutions.append(f'{activity_year}: Target={int(target)}, Average={round(avg,2)}')
    return solutions

#3h