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


if __name__ == '__main__':
    print(climb_stairs(4))
    print(climb_stairs_1(4))
