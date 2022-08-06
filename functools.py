"""
# functools:
    - Functools module is for higher-order functions that work on other functions.
    - It provides functions for working with other functions and callable
    objects to use or extend them without completely rewriting them.
    - This module has two classes – partial and partial-method.
----------------------------------------------------------------------------

1. Partial class:
    - A partial function is an original function for particular argument values.
    - They can be created in Python by using “partial” from the functools library.
    - The __name__ and __doc__ attributes are to be created by the programmer
    as they are not created automatically.
-------------------------------------------------------------------------------

Syntax:
    partial(func[, *args][, **keywords])
-------------------------------------------------------------------------------

    - Objects created by partial() have three read-only attributes:
1. partial.func:
    – It returns the name of parent function along with hexadecimal address.
2. partial.args:
    – It returns the positional arguments provided in partial function.
3. partial.keywords:
    – It returns the keyword arguments provided in partial function.
---------------------------------------------------------------------------

from functools import partial


def power(a, b):
    return a ** b


# partial functions
pow2 = partial(power, b=2)
pow4 = partial(power, b=4)
power_of_5 = partial(power, 5)

print(power(2, 3))
print(pow2(4))
print(pow4(3))
print(power_of_5(2))

print('Function used in partial function pow2: ', pow2.func)
print('Default keywords for pow2: ', pow2.keywords)
print('Default arguments for power_of_5: ', power_of_5.args)
===========================================================================

2. Partialmethod class:
    - It is a method definition of an already defined function for
    specific arguments like a partial function.
    - it is not callable but is only a method descriptor.
    - It returns a new partialmethod descriptor.
----------------------------------------------------------------------------

Syntax:
    partialmethod(func, *args, **keywords)
-----------------------------------------------------------------------

from functools import partialmethod


class Demo:
    def __init__(self):
        self.color = 'black'

    def _color(self, type):
        self.color = type

    r = partialmethod(_color, type='red')
    b = partialmethod(_color, type='blue')
    g = partialmethod(_color, type='green')


d = Demo()
print(d.color)
d.r()
print(d.color)
=====================================================================

# Functions:
1. Cmp_to_key:
    - It converts a comparison function into a key function.
    - The comparison function must return 1, -1 and 0 for different conditions.
    - It can be used in key functions such as sorted(), min(), max().
-------------------------------------------------------------------------

Syntax:
    function(iterable, key=cmp_to_key(cmp_function))
----------------------------------------------------------------------

from functools import cmp_to_key
  
# function to sort according to last character
def cmp_fun(a, b):
    if a[-1] > b[-1]:
        return 1
    elif a[-1] < b[-1]:
        return -1
    else:
        return 0
  
l1 = ['python', 'developer', 'data science']
l = sorted(l1, key = cmp_to_key(cmp_fun))
print('sorted list: ', l)
=========================================================================

2. Reduce:
    - It applies a function of two arguments repeatedly on the elements
    of a sequence so as to reduce the sequence to a single value.
---------------------------------------------------------------------------
    
Syntax:
    reduce(function, sequence[, initial]) -> value  
------------------------------------------------------------------------

from functools import reduce
l1 = [2, 4, 7, 9, 1, 3]
sum_of_l1 = reduce(lambda a, b:a + b, l1) 
print('Sum of list 1: ', sum_of_l1)
=========================================================================

3. Total_ordering:
    - It is a class decorator that fills in the missing comparison methods
    (__lt__, __gt__, __eq__, __le__, __ge__).
    - If a class is given which defines one or more comparison methods,
    “@total_ordering” automatically supplies the rest as per the given definitions.
    - the class must define one of __lt__(), __le__(), __gt__(), or __ge__() and additionally,
    the class should supply an __eq__() method.
-------------------------------------------------------------------------

from functools import total_ordering
  
@total_ordering
class N:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value
  
    # Reverse the function of 
    # '<' operator and accordingly
    # other rich comparison operators
    # due to total_ordering decorator
    def __lt__(self, other):
        return self.value > other.value
  
  
print('6 > 2 is: ', N(6)>N(2))
print('3 < 1 is: ', N(3)<N(1))
print('2 <= 7 is: ', N(2)<= N(7))
print('9 >= 10 is: ', N(9)>= N(10))
print('5 == 5 is: ', N(5)== N(5))
====================================================================

4. Update_wrapper:
    - It updates a wrapper function to look like the wrapped function.
    - update_wrapper(partial, parent).
    - This will update the documentation(__doc__) and name(__name__) of
    the partial function to same as of the parent function.
------------------------------------------------------------------------

Syntax:
    update_wrapper(wrapper, wrapped[, assigned][, updated])
--------------------------------------------------------------------

from functools import update_wrapper, partial


def power(a, b):
    ''' a to the power b'''
    return a ** b
  
# partial function
pow2 = partial(power, b = 2)
pow2.__doc__= '''a to the power 2'''
pow2.__name__ = 'pow2'
  
print('Before wrapper update -')
print('Documentation of pow2: ', pow2.__doc__)
print('Name of pow2: ', pow2.__name__)
print()
update_wrapper(pow2, power)
print('After wrapper update -')
print('Documentation of pow2: ', pow2.__doc__)
print('Name of pow2: ', pow2.__name__)
===============================================================================

5. Wraps:
    - It is a function decorator which applies update_wrapper() to the decorated function.
    - It is equivalent to partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated).
-------------------------------------------------------------------------------

from functools import wraps


def decorator(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        '''Decorator's docstring'''
        return f(*args, **kwargs)

    print('Documentation of decorated: ', decorated.__doc__)
    return decorated


@decorator
def f(x):
    '''f's Docstring'''
    return x


print('f name: ', f.__name__)
print('Documentation of f: ', f.__doc__)
========================================================================

6. LRU_cache:
    - it is a function decorator used for saving up to the maxsize
    most recent calls of a function.
    - This can save time and memory in case of repeated calls with the same arguments.
    - If *maxsize* is set to None, the cache can grow without bound.
    - If *typed* is True, arguments of different data types will be cached separately.
------------------------------------------------------------------------

Syntax :
    lru_cache(maxsize=128, typed=False)
-----------------------------------------------------------------------

from functools import lru_cache

@lru_cache(maxsize = None)
def factorial(n):
    if n<= 1:
        return 1
    return n * factorial(n-1)
print([factorial(n) for n in range(7)])
print(factorial.cache_info())
==============================================================================

7. SingleDispatch:
    - It is a function decorator.
    - It transforms a function into a generic function so that it can
    have different behaviors depending upon the type of its first argument.
    - It is used for function overloading, the overloaded implementations
    are registered using the register() attribute.
-------------------------------------------------------------------------

from functools import singledispatch

@singledispatch
def fun(s):
    print(s)
@fun.register(int)
def _(s):
    print(s * 2)

fun('DataScientist')
fun(10)
==========================================================================
"""
