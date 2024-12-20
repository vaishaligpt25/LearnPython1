from typing import List
from math import sqrt, isqrt

input_samples: List = [1, 2, 3, 4, 5, 6, 9, 14, 16, 18, 25, 27, 36, 39, 49, 64, 89, 81, 96, 144, 196]

def output_factors(n: int, factors: List[int]) -> None:
    print(f"factors of\t{n}\tare {factors}")

# ------------- implementation-1 -------------

def factors_1(n: int) -> List[int]:
    factors: List[int] = []
    for i in range(1, n + 1):
        remainder: int = n % i
        if remainder == 0:
            # i is a factor of n
            factors.append(i)
    return factors

def output_factors_1(n: int) -> None:
    output_factors(n=n, factors=factors_1(n=n))

def test_factors_1_verbose() -> None:
    separator: str = "------------- implementation-1-verbose -------------"
    print(separator)
    output_factors_1(n=1)
    output_factors_1(n=2)
    output_factors_1(n=3)
    output_factors_1(n=4)
    output_factors_1(n=5)
    output_factors_1(n=6)
    output_factors_1(n=9)
    output_factors_1(n=14)
    output_factors_1(n=18)
    output_factors_1(n=27)
    output_factors_1(n=39)
    output_factors_1(n=89)
    output_factors_1(n=96)
    print(separator)

def test_factors_1_condensed() -> None:
    separator: str = "------------- implementation-1-condensed -------------"
    print(separator)
    for n in input_samples:
        output_factors_1(n=n)
    print(separator)

# ------------- implementation-2 -------------

def factors_2(n: int) -> List[int]:
    factors: List[int] = []
    for i in range(1, int(n / 2) + 1):
        if (n % i) == 0:
            factors.append(i)
    factors.append(n)
    return factors

def output_factors_2(n: int) -> None:
    output_factors(n=n, factors=factors_2(n=n))

def test_factors_2_condensed() -> None:
    separator: str = "------------- implementation-2-condensed -------------"
    print(separator)
    for n in input_samples:
        output_factors_2(n=n)
    print(separator)

# ------------- implementation-3 -------------

def factors_3(n: int) -> List[int]:
    factors: List[int] = []
    for i in range(1, int(sqrt(n)) + 1):
        if (n % i) == 0:
            factors.append(i)

            other_factor: int = int(n / i)
            if other_factor != i:
                factors.append(other_factor)
    return factors

def factors_3_sorted(n: int) -> List[int]:
    factors: List[int] = []
    for i in range(1, int(sqrt(n)) + 1):
        if (n % i) == 0:
            factors.append(i)

            other_factor: int = int(n / i)
            if other_factor != i:
                factors.append(other_factor)
    factors: List[int] = sorted(factors)
    return factors

def output_factors_3(n: int) -> None:
    output_factors(n=n, factors=factors_3(n=n))

def test_factors_3_condensed() -> None:
    separator: str = "------------- implementation-3-condensed -------------"
    print(separator)
    for n in input_samples:
        output_factors_3(n=n)
    print(separator)

def test_factors_3_condensed_sorted() -> None:
    separator: str = "------------- implementation-3-condensed-sorted -------------"
    print(separator)
    for n in input_samples:
        output_factors(n=n, factors=factors_3_sorted(n=n))
    print(separator)

# ------------- implementation-4 -------------

def factors_4(n: int) -> List[int]:
    factors: List[int] = [i for i in range(1, n + 1) if (n % i) == 0]
    return factors

def test_factors_4_condensed() -> None:
    separator: str = "------------- implementation-4-condensed -------------"
    print(separator)
    for n in input_samples:
        output_factors(n=n, factors=factors_4(n=n))
    print(separator)

# ------------- implementation-5 -------------

# def is_factor(f: int) -> bool:
#     return (n % f) == 0

def factors_5(n: int) -> List[int]:
    natural_numbers: List[int] = range(1, n + 1)
    factors: List[int] = list(filter(lambda f: (n % f) == 0, natural_numbers))
    return factors

def test_factors_5_condensed() -> None:
    separator: str = "------------- implementation-5-condensed -------------"
    print(separator)
    for n in input_samples:
        output_factors(n=n, factors=factors_5(n=n))
    print(separator)

if __name__ == '__main__':
    test_factors_1_verbose()
    test_factors_1_condensed()
    test_factors_2_condensed()
    test_factors_3_condensed()
    test_factors_3_condensed_sorted()
    test_factors_4_condensed()
    test_factors_5_condensed()
