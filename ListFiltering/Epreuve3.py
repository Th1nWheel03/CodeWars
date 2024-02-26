def filter_list(l):
    numbers = [n for n in l if isinstance(n, int)]
    print(f'List l : {l} avec juste les nombres => list numbers : {numbers}')
    return numbers
            
filter_list([1, 2, 'aasf', '1', '123', 123])