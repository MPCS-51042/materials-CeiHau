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


#l = [int, str]
#a = int
# b = str
# # print(isinstance(1, l[0]))
# print(l[0])
# c = 1
# d = 'a'
# print(type(c) == l[0])
# print(type(b) == a)
# print(type(print.__name__))
# print(type(a))
# print(type(b))
# print(type(a) == type)
# print(10 == type)
#print(a.__name__)
