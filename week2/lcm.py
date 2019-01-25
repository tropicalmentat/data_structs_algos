# Uses python3

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def euclid_gcd(a, b):
    if b == 0:
        return a
    else:
        a_prime = a % b
        return euclid_gcd(b, a_prime)


def euclid_lcm(a, b):
    return int(a/euclid_gcd(a, b)) * b


if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())

    print(euclid_lcm(a, b))

