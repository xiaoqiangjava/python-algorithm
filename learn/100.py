#!/usr/bin/python
# -*- encoding: utf-8 -*-
from tree import TreeNode


# 相同的树
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        递归算法
        """
        return self.dfs(p, q)

    def dfs(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.dfs(p.left, q.left) and self.dfs(p.right, q.right)

    @staticmethod
    def isSameTree1(p: TreeNode, q: TreeNode) -> bool:
        """
        借助队列迭代实现
        """
        queue = [p, q]
        while queue:
            first = queue.pop(0)
            second = queue.pop(0)
            if not first and not second:
                continue
            if not first or not second:
                return False
            if first.val != second.val:
                return False
            queue.append(first.left)
            queue.append(second.left)

            queue.append(first.right)
            queue.append(second.right)

        return True
