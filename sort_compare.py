import time
import random
from sys import maxsize

def insertion_sort(alist):
    start = time.time()
    
    for index in range(1, len(alist)):
        
        current_val = alist[index]
        position = index

    while position > 0 and alist[position - 1] > current_val:
        alist[position] = alist[position - 1]
        position = position - 1
        
    alist[position] = current_val
    
    end = time.time()
    exectime = end - start

    return exectime

def shell_sort(alist):
    start = time.time()
    
    sublist_count = len(alist) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(alist, start_position, sublist_count)
        sublist_count = sublist_count // 2
    
    end = time.time()
    exectime = end - start

    return exectime

def gap_insertion_sort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        current_value = alist[i]
        position = i    
        while position >= gap and alist[position - gap] > current_value:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = current_value

def python_sort(alist):
    start = time.time()

    alist.sort()

    end = time.time()
    exectime = end - start

    return exectime

def main():
    def randlist(num):
        alist = [random.randint(1,maxsize) for x in range(0,num)]
        return alist

    list_500 = [randlist(500) for x in range(0,100)]
    list_1000 = [randlist(1000) for x in range(0,100)]
    list_10000 =  [randlist(10000) for x in range(0,100)]

    def avg_calc(func):
        spd = 0
        for x in list_500:
            result = func(x)
            spd += result
        for y in list_1000:
            result = func(y)
            spd += result
        for z in list_10000:
            result = func(z)
            spd += result
        avg = spd / 300
        print("%s took%10.7f seconds to run, on average" %(func.__name__.title(), avg))

    avg_calc(insertion_sort)
    avg_calc(shell_sort)
    avg_calc(python_sort)

if __name__ == '__main__':
    main()