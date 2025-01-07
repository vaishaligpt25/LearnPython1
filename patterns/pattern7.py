"""

x x x x x
x x x x
x x x
x x
x

"""

def show_pattern_for_n(n: int) -> None:
    print(f"Pattern for n = {n} is : ")

    for i in range (n, 0, -1):
        for j in range(i, 0, -1):
            print("x" , end=" ")
        print()
def test_cases() -> None:
    show_pattern_for_n(3)
    show_pattern_for_n(5)

if __name__ == '__main__':
    test_cases()
