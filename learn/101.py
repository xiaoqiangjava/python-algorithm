#!/usr/bin/python
# -*- encoding: utf-8 -*-
from tree import TreeNode


# 对称二叉树
class Solution:
    @staticmethod
    def isSymmetric(root: TreeNode) -> bool:
        """
        迭代实现: 按照左节点的左节点与右节点的右节点进行比较，左节点的右节点跟右节点的左节点进行比较的规则
        按照次序将节点入队，出队时比较两个节点的值是否相同，或者两个都为None
        """
        if not root:
            return True
        if not root.left and not root.right:
            return True
        queue = [root.left, root.right]
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)

        return True

    def isSymmetric1(self, root: TreeNode) -> bool:
        """
        迭代实现
        """
        if not root:
            return True
        return self.symmetric(root.left, root.right)

    def symmetric(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False

        return self.symmetric(left.left, right.right) and self.symmetric(left.right, right.left)


if __name__ == '__main__':
    node = TreeNode.TreeNode(1)
    node.left = TreeNode.TreeNode(2)
    node.right = TreeNode.TreeNode(2)
    node.left.right = TreeNode.TreeNode(3)
    node.right.right = TreeNode.TreeNode(3)
    print(Solution.isSymmetric(node))

