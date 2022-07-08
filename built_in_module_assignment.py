"""
1. math module:
        the math module has a set of methods and constants.
---------------------------------------------------------------------

# Que. if u want to check total math
import math
print(dir())
print('--------------------')
from math import *
print(dir())
----------------------------------------------------------------

import math
print(math.factorial(4))    # 24
print(math.pi)              # 3.141592653589793
print(math.log10(23))       # 1.3617278360175928
print(math.log(6))          # 1.791759469228055
-----------------------------------------------------------

import math as m
print(m.factorial(4))   # 24
print(m.pi)             # 3.141592653589793
print(m.log(10,4))          # 1.6609640474436813
print(m.pow(5, 1))          # 5.0
print(m.log10(12))          # 1.0791812460476249
-----------------------------------------------------------

from math import *
print(factorial(5))         # 120
print(e)                #  2.718281828459045
print(sin(45))          #  0.8509035245341184
print(cos(60))              # -0.9524129804151563
print(tan(90))              # -1.995200412208242
print(pow(6, 7))            # 279936.0
print(prod('5'))            # 5
--------------------------------------------------------

from math import pi , sqrt
print(pi)               # 3.141592653589793
print(sqrt(625))        # 25.0
print(sqrt(144))       # 12.0
print(sqrt(729))       # 27.0
-------------------------------------------------------

from math import factorial
print(factorial(7))       # 5040
print(factorial(9))         # 362880
print(factorial(8))         # 40320
print(factorial(3))          # 6
----------------------------------------------------------

from math import factorial as f
print(f(7))             # 5040
print(f(2))              # 2
print(f(11))            # 39916800
--------------------------------------------------------------

from math import factorial as f , sqrt as s
print(s(81))       # 9.0
print(f(1))         # 1
print(s(63))        # 7.937253933193772
print(s(141))       # 11.874342087037917
print(f(10))        # 3628800
======================================================

2. sys module:
    the sys module provides functions and variables use to manipulate
  the different part of the python.
-----------------------------------------------------------------------

# Que. if u want to check total sys
import sys
print(dir())
print('--------------------')
from sys import *
print(dir())
---------------------------------------------------------------------

import sys
print(sys.modules.fromkeys('123','num'))            # {'1': 'num', '2': 'num', '3': 'num'}
print(sys.path)
print(sys.modules)
---------------------------------------------------------------------

import sys as s
print(s.version)
print(s.argv)
print(s.modules.fromkeys('shital', 'letter'))
-----------------------------------------------------------------

from sys import *
print(version)
print(maxsize)
print(path_hooks)
-------------------------------------------------------------

from sys import stdout
print(stdout.write('python'))       # python6
print(stdout.encoding)              #utf-8
print(stdout.name)                  # <stdout>
--------------------------------------------------------

from sys import stdout as s
print(s.write('python'))       # python6
print(s.errors)                # strict
print(s.mode)                  # w
-------------------------------------------------------------

from sys import maxsize , stdin
print(maxsize)          # 9223372036854775807
print(stdin)            # <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>
print(maxsize.image)     # 0
print(stdin.encoding)   # utf-8
------------------------------------------------------------

from sys import maxsize as m, stdin as s
print(m)        # 9223372036854775807
print(s)        # <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>
============================================================

3. statistics module:
        this module use to calculate mathematical statistics of numeric data
--------------------------------------------------------------------------

# Que. if u want to check total statistics
import statistics
print(dir())
print('--------------------')
from statistics import *
print(dir())
--------------------------------------------------------------

import statistics
print(statistics.mean([1,4,3,5,6,2]))           # 3.5
print(statistics.mode([1,3,4,2,6]))             # 1
print(statistics.median_low([2,4,5,6,7,8]))     # 5
-------------------------------------------------------------

import statistics as s
print(s.median([10,20,30,40,50]))           # 30
print(s.mean([12,34,56,27,25]))             # 30.8
print(s.multimode([10,30,40,80,10]))        # [10]
---------------------------------------------------------------

from statistics import *
print(map)                         # <class 'map'>
print(staticmethod)                # <class 'staticmethod'>
print(max(1,4,5,2))                # 5
print(memoryview)                  # <class 'memory_view'>
-------------------------------------------------------------------

from statistics import median, mean
print(median((12,12,34,24,45,67)))   # 29.0
print(median({1,4,5,6,3,9,8}))         # 5
print(mean((12,12,34,24,45,67)))       # 32.333333333333336
print(mean({1,4,5,6,3,9,8}))         # 5.142857142857143
-----------------------------------------------------------

from statistics import mode
print(mode([1,2,3,7,4]))                # 1
print(mode([10,30,40,20]))              # 10
-----------------------------------------------------------

from statistics import mode as m
print(m([1,2,6,9,19,20]))           # 1
print(m({121,23,35,78,69}))         # 35
print(m([23,46,78,90]))             # 23
-------------------------------------------------------------

from statistics import mean as m , multimode as m1
print(m((12,12,34,24,45,67)))       # 32.333333333333336
print(m1([10,30,50,9,9]))           # [9]
print(m1([10,30,10,80,10]))        # [10]
print(m([12,34,56,27,25]))          # 30.8
============================================================

4. os module:
    os module in python provides functions for interacting with th operating system.
---------------------------------------------------------------------------------

# Que. if u want to check total os
import os
print(dir())
print('--------------------')
from os import *
print(dir())
------------------------------------------------------------------------

import os
print(os.name)      # nt
print(os.path)
print(os.altsep)    # /
------------------------------------------------------------------

import os as o
print(o.name)       # nt
print(o.path)
print(o.altsep)     # /
print(o.error)      # <class 'OSError'>
------------------------------------------------------------

from os import *
print(path)
print(defpath)      # .;C:\bin
--------------------------------------------------------

from os import path
print(path)     # <module 'not_path' from 'C:\\Users\\chava\\AppData\\Local\\Programs\\Python\\Python310\\lib\\ntpath.py'>
--------------------------------------------------------------------------

from os import error as e
print(e)        # <class 'OSError'>
------------------------------------------------------------------------

from os import pardir, pathsep
print(pardir)       # ..
print(pathsep)      # ;
---------------------------------------------------------------------

from os import pardir as p, pathsep as p1
print(p)        # ..
print(p1)       # ;
=========================================================================

5. array module:
     The array module defines an object type that can compactly represent an array
of some basic values as characters, integers, floating-point numbers.
---------------------------------------------------------------------------

# Que. if u want to check total array
import array
print(dir())
print('--------------------')
from array import *
print(dir())
-------------------------------------------------------------

import array
print(array.array)          # <class 'array.array'>
print(array.ArrayType)      # <class 'array.array'>
print(array.typecode)      # bBuhHiIlLqQfd
-------------------------------------------------------------------------

import array as a
print(a.array)          # <class 'array.array'>
print(a.ArrayType)      # <class 'array.array'>
print(a.typecode)      # bBuhHiIlLqQfd
--------------------------------------------------------------------------

from array import *
print(array)          # <class 'array.array'>
print(ArrayType)      # <class 'array.array'>
print(typecode)      # bBuhHiIlLqQfd
---------------------------------------------------

from array import array
print(array)        # <class 'array.array'>
------------------------------------------------

from array import array as a
print(a)        # <class 'array.array'>
-----------------------------------------------------

from array import array, typecode
print(array)
print(typecode)
----------------------------------------------------------------

from array import array as a typecode as t
print(a)            # <class 'array.array'>
print(t)            # bBuhHiIlLqQfd
==================================================================

6. itertools module:
        Itertools is a module that provides various functions that work on iterators to produce complex iterators.
-----------------------------------------------------------------------

# Que. if u want to check total itertools
import itertools
print(dir())
print('--------------------')
from itertools import *
print(dir())
---------------------------------------------------------------------

import itertools
print(itertools.count)          # <class 'itertools.count'>
print(itertools.cycle)          # <class 'itertools.cycle'>
print(itertools.repeat)         # <class 'itertools.repeat'>
---------------------------------------------------------------------

import itertools as i
print(i.count)          # <class 'itertools.count'>
print(i.cycle)          # <class 'itertools.cycle'>
print(i.repeat)         # <class 'itertools.repeat'>
print(i.product)        # <class 'itertools.product'>
------------------------------------------------------------------------

from itertools import *
print(chain)        # <class 'itertools.chain'>
print(chr(65))      # A
print(chr(90))      # Z
print(credits())
---------------------------------------------------------------------

from itertools import count
print(count)         # <class 'itertools.count'>
---------------------------------------------------------------

from itertools import count as c, chain as c1
print(c)         # <class 'itertools.count'>
print(c1)        # <class 'itertools.chain'>
-----------------------------------------------------------------

from itertools import starmap, accumulate
print(starmap)          # <class 'itertools.starmap'>
print(accumulate)       # <class 'itertools.accumulate'>
--------------------------------------------------------------------

from itertools import starmap as s, accumulate as a
print(s)          # <class 'itertools.starmap'>
print(a)          # <class 'itertools.accumulate'>
========================================================================

7. csv module:
    CSV (Common Separated Data) files to store data that are in tabular format into
plain text & each line is treated as a data record in the file.
Each record holds one or more fields separated by commas
-----------------------------------------------------------------------------

# Que. if u want to check total csv
import csv
print(dir())
print('--------------------')
from csv import *
print(dir())
----------------------------------------------------------------------------

import csv
print(csv.Error)        # <class '_csv.Error'>
print(csv.excel)        # <class 'csv.excel'>
-------------------------------------------------------------------------

import csv as c
print(c.Error)        # <class '_csv.Error'>
print(c.excel)        # <class 'csv.excel'>
-----------------------------------------------------------------------

from csv import *
print(excel)        # <class 'enumerate'>
print(excel_tab)    # <class 'csv.excel_tab'>
---------------------------------------------------------------------

from csv import field_size_limit
print(field_size_limit(10))         # 131072
print(field_size_limit(40))         # 10
------------------------------------------------------------------------

from csv import field_size_limit as f
print(f(23))                    #  40
print(f(20))                    # 3
-----------------------------------------------------------------------------

from csv import excel_tab
print(excel_tab)        # <class 'csv.excel_tab'>
----------------------------------------------------------------------------

from csv import excel_tab as e
print(e)        # <class 'csv.excel_tab'>
----------------------------------------------------------------------------

8. collections module:
        The Python collection module is defined as a container that is used to store
collections of data, for example - list, dict, set, and tuple, etc.
-----------------------------------------------------------------------------

# Que. if u want to check total collections
import collections
print(dir())
print('--------------------')
from collections import *
print(dir())
----------------------------------------------------------------------

import collections
print(collections.defaultdict)          # <class 'collections.defaultdict'>
print(collections.ChainMap)             # <class 'collections.ChainMap'>
-----------------------------------------------------------------------

import collections as c
print(c.defaultdict)          # <class 'collections.defaultdict'>
print(c.ChainMap)             # <class 'collections.ChainMap'>
------------------------------------------------------------------------

from collections import defaultdict
print(defaultdict)          # <class 'collections.defaultdict'>
----------------------------------------------------------------------

from collections import namedtuple
print(namedtuple)           # <function namedtuple at 0x00000281FA2C3880>
------------------------------------------------------------------------

from collections import defaultdict as d
print(d)          # <class 'collections.defaultdict'>
----------------------------------------------------------------------

from collections import namedtuple as n
print(n)           # <function namedtuple at 0x00000281FA2C3880>
-----------------------------------------------------------------------

from collections import defaultdict as d, namedtuple as n
print(d)          # <class 'collections.defaultdict'>
print(n)           # <function namedtuple at 0x00000281FA2C3880>
=========================================================================

9. random module:
       Python Random module is which is used to generate random numbers
--------------------------------------------------------------------------

# Que. if u want to check total random
import random
print(dir())
print('--------------------')
from random import *
print(dir())
-------------------------------------------------------------------------

import random
print(random.random())          # 0.8464505218100807
print(random.Random)            # <class 'random.Random'>
print(random.randint(1, 4))     # 3
print(random.SystemRandom)      # <class 'random.SystemRandom'>
------------------------------------------------------------------------

import random as r
print(r.getstate())
print(r.uniform(1,3))       # 1.3197634158664553
-----------------------------------------------------------------------

from random import randint
print(randint(2, 5))        # 4
print(randint(6, 9))        # 9
-----------------------------------------------------------------------

from random import randint as r
print(r(4, 6))      # 5
print(r(6, 9))      # 6
-----------------------------------------------------------------------

from random import randint as r,  random as r1
print(r(4, 6))      # 5
print(r(6, 9))      # 6
print(r1.getstate())
print(r1.uniform(1, 3))
====================================================================
"""
