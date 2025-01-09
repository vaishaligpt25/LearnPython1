"""
1
  2
    3
      4
        5

"""

def show_pattern_for_n(n: int) -> None:
    print(f"Pattern for n = {n} is:")

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i)
