#!/usr/bin/python
# -*- encoding: utf-8 -*-
from typing import List


# 接雨水
class Solution(object):
    def trap_1(self, height: List[int]) -> int:
        """
        暴力解法思路：当前索引位置能够装的水量由当前索引位置左右两边的最高值中最小的高度决定，即min(left_max, right_max)
        按照这种想法，从当前位置开始分别向左右两边查找最大值，找到其中较小的高度，减去当前位置的高度就是当前索引位置可以接的
        水的最大值(木桶效应，水量有最短的木板决定)，需要注意的是左右两边找出的最大值要不当前元素的高度大，否则容纳的水量为0
        时间复杂度：O(n^2)  这种解法超出时间限制
        空间复杂度：O(1)
        这种方式是一列一列计算可以容纳的水量
        """
        n = len(height)
        res = 0
        for idx in range(1, n):
            left_max = right_max = 0
            # 查找当前索引左边的最大值
            for i in range(0, idx):
                left_max = max(height[i], left_max, height[idx])
            # 查找当前索引右边的最大值
            for j in range(idx, n):
                right_max = max(height[j], right_max)
            # 计算当前索引位置可以容纳的水量
            res += min(left_max, right_max) - height[idx]

        return res

    def trap(self, height: List[int]) -> int:
        """
        上面的暴力解法每次都需要计算左右两边的最大值，时间复杂度为O(n^2),可以使用空间换时间, 使用单调栈将时间复杂度
        降到O(n), 空间复杂度为O(n)
        这种思路是一层一层的计算可以容纳的水量, 需要注意的是当栈中只有一个元素时，左边没有最大值，所以纳水量为0
        使用单调递减的栈，栈顶的元素时栈中最小的元素，如果新元素大于栈顶的元素，则对于栈顶元素来说，右边存在大于当前高度的
        值，左边也存在大于当前高度的值，那么久可以计算当前栈顶元素可以容纳的水量，这样一层层累加得到总的容水量
        """
        stack, n = [], len(height)
        res = 0
        for idx in range(n):
            while stack and height[idx] > height[stack[-1]]:
                top = stack.pop()
                if stack:
                    res += (min(height[idx], height[stack[-1]]) - height[top]) * (idx - stack[-1] - 1)
            stack.append(idx)

        return res


if __name__ == '__main__':
    solution = Solution()
    test = [4, 2, 0, 3, 2, 5]
    print(solution.trap(test))
