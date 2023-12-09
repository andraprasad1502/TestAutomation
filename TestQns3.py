"""
1. Decorators
2. Generators
"""
import time
import logging


#######################################################################
#func = function

def dec_func_1(func):
    def inner_func(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)  # function(a, b)
        print("end")
        return result
    return inner_func


def dec_func_2(*arg):
    def outer_func(func):
        def inner_func(*args, **kwargs):
            print("Start")
            logging.info("HELLO")
            logging.debug("DEBUG")
            logging.error('ERROR')
            logging.warning('WARNING')
            time.sleep(arg[0])
            result = func(*args, **kwargs)
            print("end")
            return result
        return inner_func
    return outer_func


#######################################################################
def gen_function(num):

    for i in range(num):
        print("Iteration", i)
        yield i*i


#######################################################################
@dec_func_1
def function(a, b):
    print("Inside Function")
    return a+b


@dec_func_2(1)
def function2(a, b):
    print("Inside function2")
    return a*b


if __name__ == '__main__':
    print('sum', function(5, 10))
    #print('mul', function2(3, 4))

    #fun = gen_function(10)
    #print(next(fun))
    #print(next(fun))
    #while True:
    #    try:
    #        print(next(fun))
    #    except Exception as e:
    #        print(str(e))
    #        print("Hello")
    #        break

