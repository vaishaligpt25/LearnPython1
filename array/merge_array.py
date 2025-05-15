from typing import List


class Solution:
    def merge1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        merged_list = sorted(nums1 + nums2)
        return merged_list

    def merge2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        merged: List[int] = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
        return merged


class SolutionTest:
    def check_merge2(self) -> None:
        soln: Solution = Solution()
        assert soln.merge1(nums1=[1, 2, 3], nums2=[3, 4, 5]) == [1, 2, 3, 3, 4, 5]
        assert soln.merge1(nums1=[], nums2=[1]) == [1]
        assert soln.merge1(nums1=[3, 4, 5], nums2=[1, 2, 3, 4]) == [1, 2, 3, 3, 4, 4, 5]

        assert soln.merge2(nums1=[1, 2, 3], nums2=[3, 4, 5]) == [1, 2, 3, 3, 4, 5]
        assert soln.merge2(nums1=[], nums2=[1]) == [1]
        assert soln.merge2(nums1=[3, 4, 5], nums2=[1, 2, 3, 4]) == [1, 2, 3, 3, 4, 4, 5]


if __name__ == '__main__':
    soln_test: SolutionTest = SolutionTest()
    soln_test.check_merge2()
