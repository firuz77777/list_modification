def remove_negative(lst):
    '''Given a list of numbers, write a function that returns a new list where all the negative numbers are removed.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list without negative numbers.
    '''
    a = []
    for i in lst:
        if i > 0:
            a.append(i)
    return a