# Uses python3

import sys


def max_dot_product(a, b):
    # write your code here

    sorted_a = sorted(a)
    sorted_b = sorted(b)

    res = 0
    for i in range(len(sorted(a))):
        res += sorted_a[i] * sorted_b[i]
    return res


if __name__ == '__main__':
    input = sys.stdin.read()

    input1 = "3,1,3,-5,-2,4,1"
    input2 = "1,23,39"

    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))

