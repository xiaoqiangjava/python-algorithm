#!/usr/bin/python
# -*- encoding: utf-8 -*-


# 二叉树
from typing import List


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preOrder(self, root: TreeNode, result: List[int]) -> List[int]:
        """
        前序遍历：递归
        """
        if not root:
            return result
        result.append(root.val)
        self.preOrder(root.left, result)
        self.preOrder(root.right, result)
        return result

    def inOrder(self, root: TreeNode, result: List[int]) -> List[int]:
        """
        中序遍历：递归
        """
        if not root:
            return result
        self.inOrder(root.left, result)
        result.append(root.val)
        self.inOrder(root.right, result)
        return result

    def postOrder(self, root: TreeNode, result: List[int]) -> List[int]:
        """
        后序遍历：递归
        """
        if not root:
            return result
        self.postOrder(root.left, result)
        self.postOrder(root.right, result)
        result.append(root.val)
        return result

    @staticmethod
    def preOrderTraversal(root: TreeNode) -> List[int]:
        """
        前序遍历：迭代
        """
        result = []
        stack = []
        while root or stack:
            if root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop(-1).right

        return result

    @staticmethod
    def inOrderTraversal(root: TreeNode) -> List[int]:
        """
        中序遍历：迭代
        """
        result = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                top = stack.pop(-1)
                result.append(top.val)
                root = top.right
        return result

    @staticmethod
    def postOrderTraversal(root: TreeNode) -> List[int]:
        """
        后序遍历：迭代
        """
        result = []
        stack = []
        last_visit = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                top = stack[-1]
                if not top.right or last_visit == top.right:    # 当前节点的右子树为null或者已经被访问过
                    result.append(top.val)
                    stack.pop(-1)
                    last_visit = top  # 标记最后一个访问的元素
                else:
                    root = top.right

        return result


if __name__ == '__main__':
    solution = Solution()
    node = TreeNode(6)
    node.left = TreeNode(2)
    node.right = TreeNode(7)
    node.left.left = TreeNode(1)
    node.left.right = TreeNode(4)
    node.left.right.left = TreeNode(3)
    node.left.right.right = TreeNode(5)
    node.right.right = TreeNode(9)
    node.right.right.left = TreeNode(8)

    print(solution.preOrder(node, []))
    print(Solution.preOrderTraversal(node))
    print(solution.inOrder(node, []))
    print(Solution.inOrderTraversal(node))
    print(solution.postOrder(node, []))
    print(Solution.postOrderTraversal(node))
