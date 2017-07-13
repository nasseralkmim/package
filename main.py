"""
Added this folder to path with:

    >>> import sys
    >>> sys.path.append("C:/Users/Nasser/Desktop/package/")

so we ce import package. Then imported `package`, this will run 
`package/__init__.py`, which will run

    >>> import package.module1

this will make package.module1 available. module1 calls a function in 
`package/subpackage/module2.py`. So we need to import module2 inside module1

    >>> import package.subpackage.module2

"""
import sys
sys.path.append("C:/Users/Nasser/Desktop/package/")

import package.module1
import package.subpackage.module2

package.module1.func_a()
sum = package.subpackage.module2.func_1()
