"""
x x x x x
x       x
x       x
x       x
x x x x x


"""

def show_pattern_for_n(n: int) -> None:
    print(f"Pattern for n ={n} is:")

    for i in range(n, 0, -1):
        if i == n :
           for j in range(n, 0, -1):
             print("x",end="  ")
           print()
        elif i == 1:
            for j in range(n, 0, -1):
                print("x", end="  ")
            print()
        else:
          for j in range(i,i+1):
              print("x       x",end=" ")
          print()



def test_cases() -> None:
    show_pattern_for_n(15)


if __name__ == '__main__':
    test_cases()