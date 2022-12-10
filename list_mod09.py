def square_and_remove_positive(lst):
    '''Given a list of numbers, write a function that returns a new list where all the numbers are squared and all the positive numbers are removed.
    
    Args:
        lst (list): list of numbers.
    
    Returns:
        list: list of all non-negative numbers ared squared.
    '''
    a = []
    for i in lst:
        if i < 0:
            a.append(i**2)
    return a