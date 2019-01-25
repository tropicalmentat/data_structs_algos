# python3
def MaxPairwiseProductNaive(numbers):

    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product

def MaxPairwiseProductFast(numbers):

    sort = sorted(numbers)
    return sort[-1] * sort[-2]

if __name__=="__main__":
    n = int(input())
    a = [int(x) for x in input().split()]
    print(MaxPairwiseProductFast(a))
