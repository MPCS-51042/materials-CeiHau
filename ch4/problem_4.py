def accepts(*types):
    for t in types:
        if type(t) != type:
            raise TypeError(f"'{t}' is not a type object.")

    def decorator(funtion):
        def wrapper(*args, **kwargs):
            for index, arg in enumerate(args):
                if (type(arg) != types[index]):
                    raise TypeError(f'Argument {arg} of {funtion.__name__} is not a {types[index].__name__}')

            return funtion(*args, **kwargs)

        return wrapper

    return decorator

#20min