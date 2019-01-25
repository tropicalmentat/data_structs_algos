# Uses python3
import sys
from math import floor
from collections import OrderedDict

def naive(a):
    for i in range(len(a)):
        count = 0
        current_elm = a[i]
        for k in range(len(a)):
            if a[k] == current_elm:
                count += 1
        if count > len(a) / 2:
            return 1
    return "no majority element"


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    # write your code here
    return -1


def countsort(a):
    # use dict as the count array with min(a) as min index
    # max(a) as max index
    # OrderedDict reduces time

    count = OrderedDict({i: i*0 for i in range(min(a), max(a)+1)})

    for i in a:
        count[i]+=1

    # for j in range(min(a)+1, max(a)+1):
    #     pos[j] = pos[j-1] + count[j-1]
    #
    # for i in a:
    #     a_prime[pos[i]-1] = i
    #     pos[i]=pos[i]+1

    # print(len(a))
    # print(max(count.values()))

    if max(count.values()) > len(a)/2:
        return 1
    else:
        return "no majority element!"


def mergecount(b, c):
    majority = []
    diff = []

    b_ = b[0]
    c_ = c[0]

    return majority


def majelm(a):
    if len(a)==1:
        return a

    mid=floor(len(a)/2)
    b = majelm(a[:mid])
    c = majelm(a[mid:])
    a_prime = mergecount(b, c)

    return a_prime


def mergesort(a):
    if len(a)==1:
        return a
    mid = floor(len(a)/2)
    b = mergesort(a[:mid])
    c = mergesort(a[mid:])
    a_prime = merge(b, c)

    return a_prime


def merge(b,c):
    d = []
    while len(b)!=0 and len(c)!=0:
        if len(b)==0 or len(c)==0:
            break
        b_ = b[0]
        c_ = c[0]
        if b<=c:
            b.remove(b_)
            d.append(b_)
        else:
            c.remove(c_)
            d.append(c_)
    d.extend(b)
    d.extend(c)
    return d


def test():
    test_in = "5 2 3 9 2 2"
    ds = list(map(int, test_in.split()))
    n = ds[0]
    a = ds[1:]

    # print(naive(a))
    # print(countsort(a))
    print(majelm(a))
    # print(mergesort(a))


def rand_test():
    import random
    random.seed()
    ds = [random.randint(i, 10) for i in range(11)]
    print(ds)
    print(mergesort(ds))
    # print(countsort(ds))
    # print(sorted(ds))
    # print(naive(sorted(ds)))


def main():

    input = sys.stdin.read()
    ds = list(map(int, input.split()))
    a = ds[1:]

    print(countsort(a))


if __name__ == '__main__':
    test()
    # rand_test()
    #
    # main()