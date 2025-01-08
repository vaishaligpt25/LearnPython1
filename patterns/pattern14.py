"""
1 2 3 4 5
        4
        3
        2
        1
        """


def show_pattern_for_n(n: int) -> None:
    print(f"Pattern for n = {n} is :")

    for i in range(1, n + 1):
        if i == 1:
            for j in range(i, n + 1):
                print(j, end=" ")
            print()
        else:
            print("       ",(n + 1 - i))
    print()


def test_cases() -> None:
    show_pattern_for_n(5)
    show_pattern_for_n(7)


if __name__ == '__main__':
    test_cases()