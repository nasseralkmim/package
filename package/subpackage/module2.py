"""
We can use relative imports

    >>> from .. import module1

or explicitly:

    >>> import package.module1

then when calling a function in module1 we would need

    >>> package.module1.func_a()

unless we do:

    >>> import package.module1 as module1

or

    >>> from package import module1
"""
from .. import module1


def func_2():
    print('module2 function')


def func_1():
    sum = module1.func_b(2, 3)
    print(sum, 'From module 1')
    return sum

