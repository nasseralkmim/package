"""
if we want to import only the package 

    >>> import package

and then use the modules with, `package.module1.func_a()` we need to import
the module when the package/__init__.py is run:

    >>> import package.module1

This is optional because module1 already imports module2.

    >>> import package.subpackage.module2

or we leave it empty and import the package modules explicitly

   >>> import package.module1
   >>> import package.subpackage.module2

which I prefer.
"""
