def full_paths(path_components, base_path='/'):
    results = []
    path = ''
    for l in range(len(path_components)):
        i = path_components[-l - 1]
        if isinstance(i, list):  # list of path
            temp = []
            for j in i:
                if len(results) == 0:  # results is empty
                    temp.append('/' + j)
                else:
                    for k in results:
                        temp.append('/' + j + k)
            results = temp
        else:  # single path
            if len(results) == 0:  # results is empty
                results.append('/' + i)
            else:
                for index in range(len(results)):
                    results[index] = '/' + i + results[index]
    for index, i in enumerate(results):
        results[index] = base_path[0:-1] + i

    return results


# path_components_1 = ['usr', ['lib', 'bin'], 'config', ['x', 'y', 'z']]
# result = full_paths(path_components_1)
# print(result)
# expected_1 = [
#     '/usr/lib/config/x',
#     '/usr/lib/config/y',
#     '/usr/lib/config/z',
#     '/usr/bin/config/x',
#     '/usr/bin/config/y',
#     '/usr/bin/config/z'
# ]
#
# print(result==expected_1)
#
# print(full_paths(['codes', ['python', 'c', 'c++'], ['Makefile']], base_path='/home/user/'))

#1h