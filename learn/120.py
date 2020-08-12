#!/usr/bin/python
# -*- encoding: utf-8 -*-
from typing import List


# 三角形最小路径和
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        1. 递归
        """
        return self.calculateTotal(0, 0, triangle)

    def calculateTotal(self, i: int, j: int, triangle: List[List[int]]) -> int:
        if i == len(triangle) - 1:
            return triangle[i][j]

        return min(triangle[i][j] + self.calculateTotal(i + 1, j, triangle),
                   triangle[i][j] + self.calculateTotal(i + 1, j + 1, triangle))

    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        """
        2. 递归+记忆化搜索
        """
        memo = [[None] * len(triangle[i]) for i in range(len(triangle))]
        return self.calculateTotal1(0, 0, triangle, memo)

    def calculateTotal1(self, i: int, j: int, triangle: List[List[int]], memo: List[List[int]]) -> int:
        if i == len(triangle) - 1:
            return triangle[i][j]
        if not memo[i][j]:
            memo[i][j] = min(triangle[i][j] + self.calculateTotal1(i + 1, j, triangle, memo),
                             triangle[i][j] + self.calculateTotal1(i + 1, j + 1, triangle, memo))
        return memo[i][j]

    @staticmethod
    def minimumTotal2(triangle: List[List[int]]) -> int:
        """
        3. 动态规划, 空间复杂度优化到O(n)
        """
        n = len(triangle)
        memo = triangle[n - 1]
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                memo[j] = min(triangle[i][j] + memo[j], triangle[i][j] + memo[j + 1])
        return memo[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumTotal([[46], [43, 61], [10, -16, 3], [-26, 41, 36, -72]]))
    print(solution.minimumTotal1([[46], [43, 61], [10, -16, 3], [-26, 41, 36, -72]]))
    print(Solution.minimumTotal2([[46], [43, 61], [10, -16, 3], [-26, 41, 36, -72]]))
