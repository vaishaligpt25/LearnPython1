
"""
18 = 2 x 3 x 3
42 = 2 x 3 x 7
21 = 3 x 7
63 = 3 x 3 x 7
315 = 3 x 3 x 5 x 7
"""

def show_prime_factors(n: int) -> None:
    print(f"Prime factors of {n} are: ", end="")
    factor: int = 2
    while n > 1:
        while (n % factor) == 0:
            n = n / factor
            print(f"{factor} ", end="")
        factor = factor + 1
    print()

if __name__ == '__main__':
    show_prime_factors(n=36)
    show_prime_factors(n=45)
    show_prime_factors(n=92)
    show_prime_factors(n=371)
    show_prime_factors(n=899)
