"""
1
2
3
4
5 4 3 2 1

"""

def show_pattern_for_n(n: int) -> None:
    print(f"Pattern for n = {n} is :")

    for i in range(1, n + 1):
        if i < n:
             print(i)
        else:
         for j in range(n, 0, -1):
             print(j, end=" ")
         print()
    print()

def test_cases() -> None:
    show_pattern_for_n(5)


if __name__ == '__main__':
    test_cases()
