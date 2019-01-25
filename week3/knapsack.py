# Uses python3
import sys

def get_optimal_value(capacity, weights, values):

    items = list(i*0 for i in range(len(weights)))

    value = 0.
    # write your code here
    for i in range(len(weights)):
        if capacity==0:
            return value
        item=min(weights[i], capacity)
        value=value+item*(values[i]/weights[i])
        weights[i] = weights[i]-item
        items[i]=items[i]+item
        capacity = capacity-item

    return value

def unit_weight(values, weights):
    d = {(v,w): v/w for v,w in zip(values, weights)}
    sorted_values = [key[0] for key, value in sorted(d.items(), key=lambda kv:kv[1], reverse=True)]
    sorted_weights = [key[1] for key, value in sorted(d.items(), key=lambda kv:kv[1], reverse=True)]

    return sorted_values, sorted_weights


if __name__ == "__main__":
    i = sys.stdin.read()
    ds = list(map(int, i.split()))

    n, capacity = ds[0:2]
    values = ds[2:(2 * n + 2):2]
    weights = ds[3:(2 * n + 2):2]

    # ds = \
    # [[3, 50],
    #  [60, 20],
    #  [100, 50],
    #  [120, 30]]

    # ds = [[1, 10], [500, 30]]

    # n, capacity = ds[0]
    # values = [i[0] for i in ds[1:]]
    # weights = [i[1] for i in ds[1:]]
    #
    # # print(unit_weight(values, weights))
    sorted_v, sorted_w = unit_weight(values, weights)

    opt_value = get_optimal_value(capacity, sorted_w, sorted_v)
    print("{:.4f}".format(opt_value))
    # print(opt_value)
