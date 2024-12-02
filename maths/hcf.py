
def _calculate_hcf_helper(big: int, small: int) -> int:
    dividend: int = big
    divisor: int = small

    while (dividend % divisor) != 0:
        # note that quotient is not used at all
        quotient: int = dividend / divisor
        remainder: int = dividend % divisor

        dividend: int = divisor
        divisor: int = remainder

    return divisor

def calculate_hcf_of_two_integers(num1: int, num2: int) -> int:
    big: int = num1 if (num1 > num2) else num2
    small: int = num1 if (num1 < num2) else num2
    return _calculate_hcf_helper(big=big, small=small)

def show_output_hcf(num1: int, num2: int) -> None:
    hcf: int = calculate_hcf_of_two_integers(num1=num1, num2=num2)
    print(f"hcf of {num1} and {num2} is {hcf}")

if __name__ == '__main__':
    show_output_hcf(num1=36, num2=60)
    show_output_hcf(num1=60, num2=36)
    show_output_hcf(num1=24, num2=38)
    show_output_hcf(num1=48, num2=64)
    show_output_hcf(num1=12, num2=112)
    show_output_hcf(num1=240, num2=96)
