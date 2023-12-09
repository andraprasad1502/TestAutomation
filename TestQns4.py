"""
Multi threading
"""
import os
import time
from threading import Thread
import multiprocessing


def function1(number):
    print("function1", os.getpid())
    for i in range(number):
        time.sleep(1)
        print(i)


def function2(number):
    print("function2", os.getpid())
    for i in range(number):
        time.sleep(1)
        print(i)


if __name__ == '__main__':
    t1 = Thread(target=function1, args=(5,))
    t2 = Thread(target=function2, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    print('T1 Completed')
    t2.join()
    print('T2 Completed')

    m1 = multiprocessing.Process(target=function1, args=(3,))
    m2 = multiprocessing.Process(target=function2, args=(7,))
    m1.start()
    m2.start()

    m1.join()
    print('M1 Completed')
    m2.join()
    print('M2 Completed')
