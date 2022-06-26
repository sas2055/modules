"""
1. Built-in modules

import math
print(math.factorial(4))    # 24
print(math.pi)              # 3.141592653589793
print('----------------module aliasing------------------')
import math as m
print(m.factorial(4))   # 24
print(m.pi)             # 3.141592653589793
-------------------------------------------------------------

from math import *
print(factorial(5))         # 120
print(e)                #  2.718281828459045
print(sin(45))          #  0.8509035245341184
------------------------------------------------------------

from math import pi , sqrt
print(pi)               # 3.141592653589793
print(sqrt(625))        # 25.0
-----------------------------------------------------------

from math import factorial
print(factorial(7))       # 5040
print('--------------member aliasing--------------')
from math import factorial as f
print(f(7))             # 5040
-----------------------------------------------------------

from math import factorial as f , sqrt as s
print(f(3))         # 6
print(s(81))       # 9.0
================================================================

2. user defined module:
        module created by a user as per business requirement.
----------------------------------------------------------------

import basic_python.string
print(basic_python.string.name)         # shital ajit shelar
print('--------------module aliasing-------------------')
import basic_python.string as s
print(s.age)                        # 27
-------------------------------------------------------------

from basic_python import string
print(string.name)              # shital ajit shelar
print(string.age)               # 27
-----------------------------------------------------------

from basic_python import string as s
print(s.weight)             # 45
-----------------------------------------------------------

from basic_python.string import name, pin_code
print(name)             # shital ajit shelar
print(pin_code)         # 415115
print('--------------member aliasing-------------------')
from basic_python.string import name as n, pin_code as p
print(n)                # shital ajit shelar
print(p)                # 415115
-------------------------------------------------------------

from basic_python.string import *
print(name, age, place, weight, pin_code)
=================================================================

# Que. if u want to check total math
import math
print(dir())
print('--------------------')
from math import *
print(dir())
print('--------------------')
from math import pi, sqrt, e
print(dir())
=================================================================
"""
