
"""

n = 5
1
2
3
4
5

"""

def print_numbers_till_n(n: int) -> None:
    print("the pattern for n=" + str(n) + " is:-")
    for i in range(1, n + 1):
        print(i)
    print()

# test cases
def test_cases() -> None:
    print_numbers_till_n(4)
    print_numbers_till_n(9)
    print_numbers_till_n(13)

if __name__ == '__main__':
    test_cases()
