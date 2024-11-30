
"""

n = 4
1
12
123
1234

n = 7
1
12
123
1234
12345
123456
1234567

"""

def show_pattern_for_n(n: int) -> None:
    print(f"The pattern for n={n} is:-")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
    print()

def test_cases() -> None:
    show_pattern_for_n(n=4)
    show_pattern_for_n(n=1)
    show_pattern_for_n(n=7)

if __name__ == '__main__':
    test_cases()
