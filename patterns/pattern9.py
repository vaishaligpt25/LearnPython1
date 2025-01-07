"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1

"""


def show_pattern_for_n_2(n: int) -> None:
    print(f"Pattern for n = {n} is:")
    for i in range(1, n + 1):
        for j in range(n, n - i, -1):
            print(f"{j}", end=" ")
        print()


def test_cases() -> None:
    show_pattern_for_n_2(5)
    show_pattern_for_n_2(3)


if __name__ == '__main__':
    test_cases()
