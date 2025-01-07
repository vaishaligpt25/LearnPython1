"""
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""

def show_pattern_for_n(n: int) -> None:
    print(f"Pattern for n = {n} is: ")

    for i in range (n, 0, -1):
        for j in range(i, 0, -1):
            print(i, end=" ")
        print()

def test_cases():
    show_pattern_for_n(5)
    show_pattern_for_n(8)

if __name__ == '__main__':
    test_cases()