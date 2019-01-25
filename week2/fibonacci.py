#python3

def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def fib(n):
    fibs = list()

    fibs.insert(0, 0) # insert 0
    fibs.insert(1, 1) # insert 1

    for i in range(n)[1:]:
        fibs.append(fibs[-1]+fibs[-2])

    if n<=1:
        return n
    else:
        return fibs[-1]


def fib_last_digit(n):
    fibs = list()

    fibs.insert(0, 0) # insert 0
    fibs.insert(1, 1) # insert 1

    for i in range(n)[1:]:
        fibs.append((fibs[-1]+fibs[-2])%10)

    if n<=1:
        return n
    else:
        return fibs[-1]


# for i in range(10):
    # print(calc_fib(i))
    # print(fib(i))
    # print(fib_last_digit(i))

n = int(input())

# print(fib(n))
print(fib_last_digit(n))