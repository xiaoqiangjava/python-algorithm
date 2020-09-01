#!/usr/bin/python
from typing import List


# 二分查找
class Solution:
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        """
        迭代实现
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def search1(self, nums: List[int], target: int) -> int:
        """
        递归实现
        """
        num = self.binarySearch(nums, target)
        if num == 10000:
            return -1
        else:
            return nums.index(num)

    def binarySearch(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 10000
        n >>= 1
        if nums[n] == target:
            return nums[n]
        elif nums[n] > target:
            return self.binarySearch(nums[:n], target)
        else:
            return self.binarySearch(nums[n + 1:], target)


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([-1, 0, 3, 5, 9, 12], 9))
    print(solution.search1([-1, 0, 3, 5, 9, 12], 15))

