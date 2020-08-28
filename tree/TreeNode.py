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
                root = stack.pop().right

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
                top = stack.pop()
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
                if not top.right or last_visit == top.right:  # 当前节点的右子树为null或者已经被访问过
                    result.append(top.val)
                    stack.pop()
                    last_visit = top  # 标记最后一个访问的元素
                else:
                    root = top.right

        return result

    @staticmethod
    def bfs(root: TreeNode) -> List[List[int]]:
        """
        广度优先
        """
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            size = len(queue)  # 记录当前level元素的个数
            current_nodes = []
            while size > 0:  # 处理当前层所有的元素
                temp = queue.pop(0)
                current_nodes.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                size -= 1
            result.append(current_nodes)

        return result

    def max_depth(self, root: TreeNode) -> int:
        """
        求一个树的最大深度
        """
        return self.calculate_depth(root, 1)

    def calculate_depth(self, root: TreeNode, depth: int) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return depth
        left_depth = self.calculate_depth(root.left, depth + 1)
        right_depth = self.calculate_depth(root.right, depth + 1)
        return max(left_depth, right_depth)


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
    print(Solution.bfs(node))
    print(solution.max_depth(node))
