def vectorize(func):
    def new_func(*args):
        result = []
        for arg in args:
            result.append(func(arg))
        #print(result)
        return result
    return new_func

# print(vectorize(int)(*['-1', '0', 100]))
# print(*(int, ['-1', '0', 100], [-1, 0, 100]))

#40min