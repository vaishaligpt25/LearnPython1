def reverse_digits (n : int) -> int:
    n_reverse: int = 0
    while n > 0:
        dig:int = n % 10
        n: int = int(n/10)
        n_reverse : int = (n_reverse*10) + dig
    return n_reverse

def output_reverse_digits(n : int) -> None:
    n_reverse: int = reverse_digits(n)
    print(f"reverse of {n} is {n_reverse}")

if __name__ == '__main__':
    output_reverse_digits(23)
    output_reverse_digits(30)
    output_reverse_digits(653)
    output_reverse_digits(7834)
