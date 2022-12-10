def square(lst):
    '''Given a list of numbers, write a function that returns a new list where all the numbers are squared.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list of all numbers are squared.
    '''
    a = []
    for i in lst:
        a.append(i**2)
    return a
print(square([2,3,5]))