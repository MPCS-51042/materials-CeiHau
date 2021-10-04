def find_minimum(sequence, comparator=None):
    '''
    :param sequence: a list of items (like numbers or strings) that decreases, then increases

    :param comparator (optional): a function that takes in TWO items
    and returns a boolean indicating whether the first one is smaller than the second

    :return: A tuple containing the smallest item and the index at which it occurs
    '''
    decrease = False
    increase = False
    flag = -1
    for index, value in enumerate(sequence):
        if index >= 1:
            if comparator != None:
                value = comparator(value)
                prior_vlaue = comparator(sequence[index - 1])
            else:
                prior_vlaue = sequence[index - 1]

            if increase == False and value < prior_vlaue:
                decrease = True
            elif value > prior_vlaue and decrease == True:
                if increase != True:
                    min_value = sequence[index - 1]
                    min_index = index - 1
                    increase = True
            else:
                return "Invalid Sequence"

    if increase == True and decrease == True:
        return (min_value, min_index)
    else:
        return "Invalid Sequence"


class TrainingAttempt():
    def __init__(self, id, weights, error):
        self.id = id
        self.weights = weights
        self.error = error

    def __repr__(self):
        return f'TrainingAttempt {self.id}'


def total_error(training_attempt):
    '''
    :param training_attempt: a TrainingAttempt

    :return: the error of a given TrainingAttempt
    '''
    return  training_attempt.error
