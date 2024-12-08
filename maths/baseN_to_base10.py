def convert1(repr: int, base: int) -> int:
    num: int = 0
    exp: int = 0

    while repr > 0:
        dig: int = repr % 10
        repr: int = int(repr / 10)

        num: int = (dig * pow(base, exp)) + num
        exp: int = exp + 1

    return num


def output_convert1(repr: int, base: int) -> None:
    num = convert1(repr, base)
    print(f"base{base}({repr}) in base10 is {num}")


if __name__ == '__main__':
    output_convert1(340, 7)
    output_convert1(1010, 2)
    output_convert1(10000, 2)
    output_convert1(1111, 2)
    output_convert1(786, 16)
    output_convert1(212, 6)
