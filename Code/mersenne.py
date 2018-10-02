def mersenne(p):
    return 2 ** p - 1

def test_mersenne():
    test_primes = [2, 3, 5, 7, 13, 17, 19, 31]
    test_values = [3, 7, 31, 127, 8191, 131071, 524287, 2147483647]

    for i in range(len(test_primes)):
        if mersenne(test_primes[i]) == test_values[i]:
            print("{} correct.").format(i)
        else:
            print("{} error.").format(i)

test_mersenne()
