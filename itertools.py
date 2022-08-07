"""
# itertools:
    - itertools module is used to iterate over data structures that
    can be stepped over using a for-loop.
    - Such data structures are also known as iterables.
    - This module works as a fast, memory-efficient tool that is used
    either by themselves or in combination to form iterator algebra.
-----------------------------------------------------------------------------------

Que. Why to use ?
    - This module incorporates functions that utilize computational resources efficiently.
    - Using this module also tends to enhance the readability and maintainability of the code.
---------------------------------------------------------------------------------------

# grouper Recipe:
    - The grouper() function can be found in the Recipe's section of the itertools docs.
    - The recipes are an excellent source of inspiration for ways
    to use itertools to your advantage.
-------------------------------------------------------------------

import itertools as it

# defining the grouper function
def grouper(inputs, n, fillvalue = None):
    iters = [iter(inputs)] * n
    return it.zip_longest(*iters, fillvalue = fillvalue)

alpha = ['s', 'h', 'i', 't', 'a', 'l', 'a',
         'j', 'i', 't', 's', 'h', 'e', 'l', 'a', 'r']
print(list(grouper(alpha, 3)))
============================================================================

# Brute force scenario:
    - Brute force is a straight forward method of solving a problem
    that relies on sheer computing power and trying every possibility
    rather than advanced techniques to improve efficiency.
------------------------------------------------------------------------

    -There are different Brute force itertools function such as:
1. combinations()
2. combinations_with_replacement()
3. permutations()
------------------------------------------------------------------------

1. combinations():
    - The itertools.combinations() function takes two arguments—an
    iterable inputs and a positive integer n—and produces an iterator
    over tuples of all combinations of n elements in inputs.
------------------------------------------------------------------------

import itertools as it
print(list(it.combinations([1, 2], 2)))
===========================================================================

2. combinations_with_replacement():
    - combinations_with_replacement() works just like combinations(),
    accepting an iterable inputs and a positive integer n, and returns an iterator
    over n-tuples of elements from inputs.
    - The difference is that combinations_with_replacement() allows
    elements to be repeated in the tuples it returns.
---------------------------------------------------------------------------

import itertools as it
print(list(it.combinations_with_replacement([1, 2], 2)))
============================================================================

3.permutations():
    - A permutation is a collection or a combination of objects from a
    set where the order or the arrangement of the chosen objects does matter.
    - permutations() accepts a single iterable and produces all possible
    permutations (rearrangements) of its elements.
-----------------------------------------------------------------------

import itertools as it

print(list(it.permutations(['s', 'h', 'i', 'v'])))
=============================================================================

# Flattening A List of Lists:
    - Converting a list of lists (2D), into a list (1D) is called flattening.
    - Flattening a list of lists merges all the sublists into one unified list.
--------------------------------------------------------------------------

import itertools as it

list_of_lists = [[1, 2], [3, 4]]
chain_object = it.chain.from_iterable(list_of_lists)

# Return chain object with nested lists separated
# Convert to list to flatten
flattened_list = list(chain_object)
print(flattened_list)
=======================================================================
"""