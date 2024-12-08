
"""

n = 1
^

n = 2
^
^^
^

n = 4
^
^^
^^^
^^^^
^^^
^^
^

"""

def show_pattern_for_n_method1(n: int) -> None:
    print(f"The pattern for n={n} is:-")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("^", end="")
        print()
    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print("^", end="")
        print()

    print()

def show_pattern_for_n_method2(n: int) -> None:
    print(f"The pattern for n={n} is:-")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("^", end="")
        print()
    for i in range(1, n):
        for j in range(1, n - i + 1):
            print("^", end="")
        print()

    print()

def test_cases() -> None:
    show_pattern_for_n_method1(n=4)
    show_pattern_for_n_method1(n=1)

    show_pattern_for_n_method2(n=7)
    show_pattern_for_n_method2(n=9)

if __name__ == '__main__':
    test_cases()
