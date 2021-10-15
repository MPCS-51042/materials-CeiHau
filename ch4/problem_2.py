def unique(iterable, key=None):
    uniqueness = {1}
    uniqueness.remove(1)

    for i in iterable:
        if key ==None:
            if i not in uniqueness:
                uniqueness.add(i)
                yield i
        else:
            if key(i) not in uniqueness:
                uniqueness.add(key(i))
                yield i


#10min