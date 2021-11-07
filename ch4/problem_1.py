def vectorize(func):
    def new_func(*args):
        result = []
        for arg in args:
            result.append(func(arg))
        #print(result)
        return result
    return new_func
#40min