import time
import random
from sys import maxsize

def sequential_search(alist, item):
    start = time.time()

    pos = 0
    found = False

    while pos < len (alist) and not found:
        if alist[pos] == item:
            found = True
        else: 
            pos = pos+1
    
    end = time.time()
    exectime = end - start

    return (found,exectime)

def ordered_sequential_search(alist, item):
    start = time.time()

    pos = 0
    found = False
    stop = False
    
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos+1

    end = time.time()
    exectime = end - start

    return (found,exectime)

def binary_search_iterative(alist, item):
    start = time.time()

    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end = time.time()
    exectime = end - start

    return (found, exectime)

def binary_search_recursive(alist, item):
    start = time.time()

    def bsr(alist, item):
        if len(alist) == 0:
            return False
        else:
            midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return bsr(alist[:midpoint], item)
            else:
                return bsr(alist[midpoint + 1:], item)

    found = bsr(alist, item)
    end = time.time()
    exectime = end - start

    return (found, exectime)

def main():
    def randlist(num):
        alist = [random.randint(1,maxsize) for x in range(0,num)]
        alist.sort()
        return alist

    list_500 = [randlist(500) for x in range(0,100)]
    list_1000 = [randlist(1000) for x in range(0,100)]
    list_10000 =  [randlist(10000) for x in range(0,100)]

    def avg_calc(func):
        spd = 0
        for x in list_500:
            result = func(x,-1)
            spd += result[1]
        for y in list_1000:
            result = func(y,-1)
            spd += result[1]
        for z in list_10000:
            result = func(z,-1)
            spd += result[1]
        avg = spd / 300
        print("%s took%10.7f seconds to run, on average" %(func.__name__.title(), avg))

    avg_calc(sequential_search)
    avg_calc(ordered_sequential_search)
    avg_calc(binary_search_iterative)
    avg_calc(binary_search_recursive)

if __name__ == '__main__':
    main()