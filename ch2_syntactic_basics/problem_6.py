def find_numbers():
    '''
        This function computes the combinations of the numbers, 1 through 9, for which

        ABC = A*B*C*(A+B+C)
    '''
    result = []
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                if a * 100 + b * 10 + c == a * b * c * (a + b + c):
                    result.append(f"For {a}, {b}, and {c}, the equation solution is {a}{b}{c}")

    return result
