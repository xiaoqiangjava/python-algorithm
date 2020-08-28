#!/usr/bin/python
# -*- encoding: utf-8 -*-
from tree import TreeNode


# 二叉树的最大深度
class Solution:
    def max_depth(self, root: TreeNode) -> int:
        """
        使用深度优先算法求最大深度
        """
        return self.calculate_depth(root, 1)

    def calculate_depth(self, root: TreeNode, depth: int) -> int:
        if not root:
            return 0
        if not root.right and not root.left:
            return depth
        left_depth = self.calculate_depth(root.left, depth + 1)
        right_depth = self.calculate_depth(root.right, depth + 1)

        return max(left_depth, right_depth)

    @staticmethod
    def max_depth1(self, root: TreeNode) -> int:
        """
        使用广度优先算法求最大深度
        """
        if not root:
            return 0
        depth = 0
        queue = [root]
        while queue:
            size = len(queue)
            depth += 1
            while size > 0:
                temp = queue.pop(0)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                size -= 1

        return depth


if __name__ == '__main__':
    solution = Solution()
    node = TreeNode.TreeNode(6)
    node.left = TreeNode.TreeNode(2)
    node.right = TreeNode.TreeNode(7)
    node.left.left = TreeNode.TreeNode(1)
    node.left.right = TreeNode.TreeNode(4)
    node.left.right.left = TreeNode.TreeNode(3)
    node.left.right.right = TreeNode.TreeNode(5)
    node.right.right = TreeNode.TreeNode(9)
    node.right.right.left = TreeNode.TreeNode(8)
    print(solution.max_depth(node))
    print(solution.max_depth1(node))
