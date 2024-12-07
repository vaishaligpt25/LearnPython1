def output_is_prime(n: int) -> None:
    print("is_prime(" + str(n) + ") = " + str(check_is_prime(n)))


def check_is_prime(n: int) -> bool:
    if n == 1:
        return False

    num_factors: int = 0

    # count no of factors of n
    for i in range(2, n):
        if (n % i) == 0:
            num_factors = num_factors + 1

    if num_factors == 0:
        return True
    else:
        return False


def test_is_prime() -> None:
    # these are the different test cases
    output_is_prime(1)
    output_is_prime(2)
    output_is_prime(3)
    output_is_prime(4)
    output_is_prime(5)
    output_is_prime(6)
    output_is_prime(7)
    output_is_prime(46)
    output_is_prime(71)
    output_is_prime(63)
    output_is_prime(96)
    output_is_prime(97)


if __name__ == '__main__':
    test_is_prime()
