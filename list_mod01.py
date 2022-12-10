def remove_odd(lst):
    '''Given a list of numbers, write a function that returns a new list where all the odd numbers are removed.

    Args:
        lst (list): a list of number.
    
    Returns:
        list: list without odd numbers.
    '''
    a = []
    for i in lst:
        if i % 2 == 0:
            a.append(i)
    return a
print(remove_odd([3,2,3,2,3,4]))