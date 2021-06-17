from package import module


def func_2():
    print('This is a module2 function!!')


def func_1():
    sum = module.func_b(2, 3)
    print(sum, 'From module 1')
    return sum
