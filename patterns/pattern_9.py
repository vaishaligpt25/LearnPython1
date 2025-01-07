"""
n = 4

* * * * * * *
  * * * * *
    * * *
      *
"""

def show_pattern_for_n(n: int) -> None:
    print(f"Pattern for n = {n} is: ")

    for i in range(1, n+1):
        for space in range(i):
            print("  ", end="")
        for j in range((n - i)*2 - 1):
            print("*", end= " ")
        print()

def test_cases() -> None:
    show_pattern_for_n(n =4)
    show_pattern_for_n(n =6)



if __name__ == '__main__':
    test_cases()