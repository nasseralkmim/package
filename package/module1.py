"""
If I did this:

    >>> import sys
    >>> sys.path.append("C:/Users/Nasser/Desktop/package/package")
    >>> import subpackage.module2

then the folder (package) `subpackage` would be in the path.
But its better to do the following:

    >>> import package.subpackage.module2

Beucase I only need to add the package folder to path.
"""
# import package.subpackage.module2
from .subpackage import module2


def func_a():
    module2.func_2()
    

def func_b(a,  b):
    return a + b
