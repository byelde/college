import doctest

def soma(a,b):
    '''
    >>> soma(3,2)
    5
    >>> soma(2,3)
    5
    >>> soma(10,5)
    15
    '''
    s = a + b
    return s

def sub(a,b):
    '''
    >>> sub(3,2)
    1
    >>> sub(2,3)
    -1
    >>> sub(10,5)
    5
    '''
    s = a - b
    return s

def mult(a,b):
    '''
    >>> mult(10,5)
    50
    >>> mult(2,4)
    8
    >>> mult(7,6)
    42
    '''
    m = a*b
    return m

def div(a,b):
    '''
    >>> div(9,3)
    3.0
    >>> div(8,1)
    8.0
    >>> div(8,2)
    4.0
    '''
    d = a/b
    return d

def fact(b):
    '''
    >>> fact(5)
    120
    >>> fact(4)
    24
    >>> fact(3)
    6
    '''
    f = 1
    for c in range(b,0,-1):
        f *= c
    return f

if __name__ == "__main__":
    doctest.testmod()