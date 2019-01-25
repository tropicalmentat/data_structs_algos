# Uses python3

def get_change(m):

    amt = m  # amount to change into coins
    coins = [10, 5, 1]
    change = list()

    # get inputs 1 and 0 out of the way
    if m==0:
        return 0
    elif m==1:
        return 1

    diff = amt
    # get largest coin that gives a difference > 0 with amt
    while sum(change)!=m:
        for coin in coins:  # look for the coin with a value less than input value and can minimize difference
            if diff<0:
                pass
            elif amt==coin:  # continue with iteration to break amt==coins into smaller coins
                continue
            elif diff>0 and coin<=diff:
                change.append(coin)
                diff -= coin
                break # break to reset iteration of coin list

    return len(change), change

def test_alg(n):
    print("testing money change algorithm")
    for i in range(n):
        print(i,get_change(i))
    return

if __name__ == '__main__':
    # m = int(input())
    # print(get_change(m))
    print(get_change(5))
    # test_alg(17)