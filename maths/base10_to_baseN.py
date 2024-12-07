from typing import List


def convert_wrong(n: int, base: int) -> None:
    while n > 0:
        remainder: int = n % base
        print(remainder, end="")

        n: int = int(n / base)
    print()


def output_convert_wrong(n: int, base: int) -> None:
    print(f"base {base} representation of {n} is ")

    convert_wrong(n=n, base=base)


def convert(num: int, base: int) -> List[int]:
    remainders_list: List[int] = []
    while num > 0:
        remainder: int = num % base
        remainders_list.append(remainder)

        num: int = int(num / base)

    remainders_list.reverse()
    return remainders_list


def output_convert_1(num: int, base: int) -> None:
    remainders_list = convert(num=num, base=base)
    print(f"base {base} representation of {num} is: " + str(remainders_list))


def output_convert_2(num: int, base: int) -> None:
    remainders_list = convert(num=num, base=base)
    print(f"base {base} representation of {num} is: ", end="")

    for i in range(0, len(remainders_list)):
        print(remainders_list[i], end="")

    print()


def output_convert_3(num: int, base: int) -> None:
    remainders_list = convert(num=num, base=base)
    print(f"base {base} representation of {num} is: ", end="")

    for digit in remainders_list:
        print(digit, end="")

    print()


def output_convert_4(num: int, base: int) -> None:
    remainders_list: List[int] = convert(num=num, base=base)

    num_converted: str = ""
    for digit in remainders_list:
        num_converted: str = num_converted + str(digit)

    print(f"base {base} representation of {num} is: {num_converted}")


def output_convert_5(num: int, base: int) -> None:
    remainders_list: List[int] = convert(num=num, base=base)
    remainders_list_str: List[str] = [str(digit) for digit in remainders_list]
    num_converted: str = "".join(remainders_list_str)
    print(f"base {base} representation of {num} is: {num_converted}")


def output_convert_6(num: int, base: int) -> None:
    remainders_list: List[int] = convert(num=num, base=base)
    remainders_list_str: List[str] = [str(digit) for digit in remainders_list]
    num_converted_str: str = "".join(remainders_list_str)
    num_converted_int: int = int(num_converted_str)
    print(f"base {base} representation of {num} is: {num_converted_int}")


def convert_int_1(num: int, base: int) -> int:
    # determine representation of num in base(base) in form of a List[int]
    remainders_list: List[int] = []
    while num > 0:
        remainder: int = num % base
        remainders_list.append(remainder)

        num: int = int(num / base)

    remainders_list.reverse()

    # convert List[int] into int
    remainders_list_str: List[str] = [str(digit) for digit in remainders_list]
    num_converted_str: str = "".join(remainders_list_str)
    num_converted_int: int = int(num_converted_str)

    return num_converted_int


def output_convert_7(num: int, base: int) -> None:
    num_converted_int: int = convert_int_1(num=num, base=base)
    print(f"base {base} representation of {num} is: {num_converted_int}")


def convert_int_2(num: int, base: int) -> int:
    # determine representation of num in base(base) in form of a List[str]
    remainders_list_str: List[str] = []
    while num > 0:
        remainder: int = num % base
        remainders_list_str.append(str(remainder))

        num: int = int(num / base)
    remainders_list_str.reverse()

    # convert List[str] into int
    num_converted_str: str = "".join(remainders_list_str)
    num_converted_int: int = int(num_converted_str)

    return num_converted_int


def output_convert_8(num: int, base: int) -> None:
    num_converted_int: int = convert_int_2(num=num, base=base)
    print(f"base {base} representation of {num} is: {num_converted_int}")


if __name__ == '__main__':
    print("------wrong-----")
    output_convert_wrong(n=175, base=7)
    output_convert_wrong(n=12, base=2)
    print("-----------")

    print("------1-----")
    output_convert_1(num=175, base=7)
    output_convert_1(num=12, base=2)
    print("-----------")

    print("------2-----")
    output_convert_2(num=175, base=7)
    output_convert_2(num=12, base=2)
    print("-----------")

    print("------3-----")
    output_convert_3(num=175, base=7)
    output_convert_3(num=12, base=2)
    print("-----------")

    print("------4-----")
    output_convert_4(num=175, base=7)
    output_convert_4(num=12, base=2)
    print("-----------")

    print("------5-----")
    output_convert_5(num=175, base=7)
    output_convert_5(num=12, base=2)
    print("-----------")

    print("------6-----")
    output_convert_6(num=175, base=7)
    output_convert_6(num=12, base=2)
    print("-----------")

    print("------7-----")
    output_convert_7(num=175, base=7)
    output_convert_7(num=12, base=2)
    print("-----------")

    print("------8-----")
    output_convert_8(num=175, base=7)
    output_convert_8(num=12, base=2)
    print("-----------")
