#!/usr/bin/python
# -*- encoding: utf-8 -*-


# 计算x的n次幂函数
def my_pow(x: float, n: int) -> float:
    """
    使用分治算法实现: O(log(n))
    """
    # 递归终止条件
    if n == 0:
        return 1
    if n == 1:
        return x
    # 负数
    if n < 0:
        return 1 / my_pow(x, -n)
    # 偶数
    if n & 1 == 0:
        return my_pow(x * x, n // 2)
    # 奇数
    else:
        return x * my_pow(x, n - 1)


def my_flow_1(x: float, n: int) -> float:
    """
    brute force: O(n)
    """
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        return 1 / my_flow_1(x, -n)
    res = 1
    for _ in range(1, n+1):
        res *= x

    return res


if __name__ == '__main__':
    print(my_flow_1(2, -3))
    print(my_pow(2, 10))
