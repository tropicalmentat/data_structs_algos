# Uses python3
import sys
from math import floor

def iter_bisearch(a,x):
    high = len(a)-1
    low = 0

    while low <= high:
        mid = floor(low+((high - low) / 2))
        if x==a[mid]:
            return mid
        elif x<a[mid]:
            high=mid-1
        elif x>a[mid]:
            low=mid+1
    return -1


def binary_search(a, x):
    # sort the array
    # get the lowest, highest and mid index
    return


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


def stress_test():
    import random
    # set random N
    N = random.randint(1, 50)
    # generate random array
    a = [random.randint(0,i) for i in range(5,N)]
    # generate random inputs
    x = [random.randint(0,j) for j in range(5,N)]

    for number in x:
        # print(linear_search(a,number)==binary_search(a,number))
        print(iter_bisearch(sorted(a), number), end=' ')

    print('\n')

    for number in x:
        # print(binary_search(a, number), end=' ')
        print(linear_search(sorted(a), number), end=' ')


def eg_input():
    input1 = "5 1 5 8 12 13 5 8 1 23 1 11"
    #
    data = list(map(int, input1.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]

    for x in data[n + 2:]:
        print(iter_bisearch(a,x), end=' ')

    print('\n')

    for x in data[n + 2:]:
        print(linear_search(a, x), end=' ')

    return


def main():
    input = sys.stdin.read()

    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        # print(linear_search(a, x), end=' ')
        # print(binary_search(a, x), end=' ')
        print(iter_bisearch(a, x))


if __name__ == '__main__':
    main()
    # stress_test()
    # eg_input()
