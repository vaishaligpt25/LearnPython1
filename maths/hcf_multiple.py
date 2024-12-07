from typing import List
from hcf import calculate_hcf_of_two_integers

"""
      [0]  [1] [2] [3]  
input=[32, 48, 60, 100]
output=4
"""


def calculate_hcf(nums: List[int]) -> int:
    list_len: int = len(nums)
    if list_len == 0:
        # error
        return -1
    elif list_len == 1:
        # base-case
        return nums[0]
    else:
        old_hcf: int = calculate_hcf_of_two_integers(num1=nums[0], num2=nums[1])
        for i in range(2, list_len):
            new_hcf: int = calculate_hcf_of_two_integers(num1=old_hcf, num2=nums[i])
            old_hcf: int = new_hcf
        return old_hcf


def show_output_hcf(nums: List[int]) -> None:
    hcf: int = calculate_hcf(nums=nums)
    print(f"HCF of numbers {nums} is {hcf}")


if __name__ == '__main__':
    show_output_hcf(nums=[])
    show_output_hcf(nums=[56])
    show_output_hcf(nums=[56, 21])
    show_output_hcf(nums=[56, 14, 21])
    show_output_hcf(nums=[56, 14, 21, 4])
    show_output_hcf(nums=[100, 32, 60, 48])
    show_output_hcf(nums=[100, 32, 60, 48, 36])
