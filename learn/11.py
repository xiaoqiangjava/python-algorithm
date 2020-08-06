#!/usr/bin/python
# -*- encoding: utf-8 -*-
from typing import List


# 盛最多水的容器
def max_area(height: List[int]) -> int:
    """
    双指针解法
    """
    left, right, res = 0, len(height) - 1, 0
    while left < right:
        if height[left] < height[right]:
            res = max(res, height[left] * (right - left))
            left += 1
        else:
            res = max(res, height[right] * (right - left))
            right -= 1

    return res


if __name__ == '__main__':
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
