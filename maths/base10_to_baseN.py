def convert_wrong(n: int ,base: int) -> None:
    while n > 0:
        remainder : int = n % base
        print(remainder, end="")

        n : int = int (n/ base)
    print()

def output_convert_wrong(n: int ,base: int) -> None:
    print(f"base {base} representation of {n} is ")

    convert_wrong(n=n, base=base)

if __name__ == '__main__':
    output_convert_wrong(n=175, base=7)
    output_convert_wrong(n=12, base=2)