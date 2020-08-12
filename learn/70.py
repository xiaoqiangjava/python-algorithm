#!/usr/bin/python
# -*- encoding: utf-8 -*-


# 爬楼梯，每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？n阶台阶
def climb_stairs(n: int) -> int:
    """
    1. 使用动态规划思路，爬到最后一个楼梯，可以走一步，也可以走两步，所以得到如下动态转移方程：
    f(n) = f(n-1) + f(n-2)
    """
    if n < 2:
        return 1
    first, second = 1, 1
    for _ in range(2, n + 1):
        first, second = second, first + second

    return second


def climb_stairs_1(n: int) -> int:
    """
    2. 使用递归解法, 类似于斐波拉契队列
    """
    if n < 2:
        return 1
    return climb_stairs(n - 1) + climb_stairs(n - 2)


def climb_stairs_2(n: int) -> int:
    """
    在递归的基础之上，使用记忆化搜索
    """
    memo = [-1 for _ in range(n + 1)]
    calculate(n, memo)

    return memo[n]


def calculate(n: int, memo: list) -> int:
    if n < 2:
        return 1
    if memo[n] == -1:
        memo[n] = calculate(n - 1, memo) + calculate(n - 2, memo)
    return memo[n]


def climb_stairs_3(n: int) -> int:
    """
    动态规划，记录所有中间结果
    """
    if n < 2:
        return 1
    memo = [-1 for _ in range(n + 1)]
    memo[0], memo[1] = 1, 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


if __name__ == '__main__':
    print(climb_stairs(4))
    print(climb_stairs_1(4))
    print(climb_stairs_2(4))
    print(climb_stairs_3(4))
