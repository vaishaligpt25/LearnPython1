"""
* * * * * * *
  * * * * *
    * * *
      *
"""

# n is 1-indexed; so that 1st odd number is 1
def get_nth_odd_number(n: int) -> int:
    return (2 * n) - 1


def show_pattern_for_n_2(n: int) -> None:
    for i in range(n, 0, -1):
        # print spaces before X's
        for j in range(1, n - i + 1):
            print("..", end="")

        # print X's in between
        num_of_x_to_print: int = get_nth_odd_number(n=i)
        for j in range(1, num_of_x_to_print + 1):
            if j == num_of_x_to_print:
                print("x", end="")
            else:
                print("x ", end="")

        # print spaces after- X's
        for j in range(1, n - i + 1):
            print("..", end="")

        print()


def show_pattern_for_n_1(n: int) -> None:
    print(f"Pattern for n = {n} is: ")

    for i in range(1, n+1):
        for space in range(i):
            print("  ", end="")
        for j in range((n - i)*2 - 1):
            print("*", end= " ")
        print()



def test_cases() -> None:
    show_pattern_for_n_1(5)
    show_pattern_for_n_1(8)


if __name__ == '__main__':
    test_cases()
