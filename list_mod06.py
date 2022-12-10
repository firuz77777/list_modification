def square_and_remove_even(lst):
    '''Given a list of numbers, write a function that returns a new list where all the numbers are squared and all the even numbers are removed.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list of all even numbers are squared.
    '''
    a = []
    for i in lst:
        if i % 2 == 1:
            a.append(i**2)
    return a
    