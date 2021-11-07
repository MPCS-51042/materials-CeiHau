def maketuple(function):
    def wrapper(*args, **kwargs):
        return_val = function(*args, **kwargs)
        l = []
        try:
            for i in return_val:
                l.append(i)
        except TypeError:
            l.append(return_val)
        t = tuple(l)
        return t

    return wrapper


# 20min
