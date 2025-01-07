"""
1
x	x
1	2	3
x	x	x	x
1	2	3	4	5

"""

def show_pattern_for_n(n: int) -> None:
    print(f"Pattern for n = {n} is: ")

    for i in range(1, n + 1):
        if i % 2 == 0:
          for j in range (1, i + 1):
            print("x", end=" ")
          print()
        else:
          for j in range (1, i + 1):
            print(j, end=" ")
          print()
    print()

def test_cases() -> None:
    show_pattern_for_n(3)
    show_pattern_for_n(8)

if __name__ == '__main__':
    test_cases()
