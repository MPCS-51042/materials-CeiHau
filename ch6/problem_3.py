import functools


class Stream:
    def __init__(self, lst):
        self.lst = lst

    def as_list(self):
        return self.lst

    def map(self, expression):
        self.lst = list(map(expression, self.lst))
        print(f'self.lst = {self.lst}')
        return self

    def filter(self, condition):
        self.lst = list(filter(condition, self.lst))

        return self

    def reduce(self, function):
        for index in range(len(self.lst)):
            if index == 0:
                result = self.lst[0]
            else:
                result = function(result, self.lst[index])
        return result
        # return functools.reduce(function,self.lst)


print(list(filter(lambda x: len(x) < 9, ["holy", "forking", "shirtballs"])))
