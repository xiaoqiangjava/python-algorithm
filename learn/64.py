#!/usr/bin/python
# -*- encoding: utf-8 -*-
from typing import List


# 最小路径和：m * n的网格，每次只能向右或者向下移动一步，求总和最小的路径
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        1. 递归解法
        """
        return self.calculateMin(0, 0, grid)

    def calculateMin(self, m: int, n: int, grid: List[List[int]]) -> int:
        # 递归终止条件
        if m == len(grid) - 1 and n == len(grid[m]) - 1:
            return grid[m][n]
        if m == len(grid) - 1:
            return grid[m][n] + self.calculateMin(m, n + 1, grid)
        if n == len(grid[m]) - 1:
            return grid[m][n] + self.calculateMin(m + 1, n, grid)

        return grid[m][n] + min(self.calculateMin(m + 1, n, grid), self.calculateMin(m, n + 1, grid))

    def minPathSum1(self, grid: List[List[int]]) -> int:
        """
        2. 递归+记忆化搜索
        """
        memo = [[None] * len(grid[m]) for m in range(len(grid))]
        return self.calculateMin1(0, 0, grid, memo)

    def calculateMin1(self, m: int, n: int, grid: List[List[int]], memo: List[List[int]]) -> int:
        # 递归终止条件
        if m == len(grid) - 1 and n == len(grid[m]) - 1:
            return grid[m][n]
        if m == len(grid) - 1:
            if not memo[m][n]:
                memo[m][n] = grid[m][n] + self.calculateMin1(m, n + 1, grid, memo)
            return memo[m][n]
        if n == len(grid[m]) - 1:
            if not memo[m][n]:
                memo[m][n] = grid[m][n] + self.calculateMin1(m + 1, n, grid, memo)
            return memo[m][n]
        if not memo[m][n]:
            memo[m][n] = grid[m][n] + min(self.calculateMin1(m + 1, n, grid, memo),
                                          self.calculateMin1(m, n + 1, grid, memo))
        return memo[m][n]

    @staticmethod
    def minPathSum2(grid: List[List[int]]) -> int:
        """
        动态规划
        """
        memo = [[-1] * len(grid[m]) for m in range(len(grid))]
        m = len(grid)
        n = len(grid[m - 1])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    memo[i][j] = grid[i][j]
                elif i == m - 1:
                    memo[i][j] = grid[i][j] + memo[i][j + 1]
                elif j == n - 1:
                    memo[i][j] = grid[i][j] + memo[i + 1][j]
                else:
                    memo[i][j] = grid[i][j] + min(memo[i][j + 1], memo[i + 1][j])
        return memo[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
    print(solution.minPathSum1([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
    print(solution.minPathSum2([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
