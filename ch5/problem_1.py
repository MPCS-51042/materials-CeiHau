class SwiftArray(list):
    def allSatisfy(self, predicate):
        for i in self:
            if predicate(i) == False:
                return False
        return True

    def drop(self, predicate):
        result = []
        for i in self:
            if predicate(i) == False:
                result.append(i)
        return result

    def min(self, by=None):
        min = self[0]
        for i in self:
            if by == None:
                if i < min:
                    min = i
            else:
                if by(i, min):
                    min = i
        return min

    def partition(self, predicate):
        tag = False
        tail = []
        for index, i in enumerate(self):
            if (predicate(i) == True):
                self.remove(i)
                tail.append(i)
        index = len(self)
        self.extend(tail)
        return index


# dir(list)
# dir(list.__name__)
# print(list.__class__)
# print(list.__mro__)
# print(dir(list))
# print([1, 2, 3].__contains__(0))
#
# print(isinstance(SwiftArray([33]), list))
# print(isinstance(SwiftArray([33]), SwiftArray))
# print(SwiftArray([1, 2, 3, 4]).allSatisfy(lambda x: x < 3))
# print(SwiftArray([1, 2, 3, 4]).allSatisfy(lambda x: type(x) == int))
# print(SwiftArray([1, 2, 3, 4]).drop(lambda x: x < 3))
# print(SwiftArray([1, 2, -1, 4]).min())
# print(SwiftArray(['bb', 'a', 'ccc']).min(lambda x, y: len(x) < len(y)))
# x = SwiftArray([1, -3, 10, 5])
# print(x.min(lambda a, b: abs(a) < abs(b)))
# print(x.min(lambda a, b: a > b))
# print(SwiftArray([1, 2, 3, 4]).partition(lambda x: x < 2))
#
# first = x.partition(lambda v: v < 0)
# print(x)
# print(x[first])

# 30min
