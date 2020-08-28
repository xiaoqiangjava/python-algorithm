#!/usr/bin/python
# -*- encoding: utf-8 -*-
from typing import List
from tree import TreeNode


# 从底部向顶部层级遍历二叉树
class Solution:
    @staticmethod
    def levelOrderBottom1(root: TreeNode) -> List[List[int]]:
        """
        使用栈辅助实现
        """
        if not root:
            return []
        result = []
        stack = []
        queue = [root]
        while queue:
            size = len(queue)
            nodes = []
            while size > 0:
                temp = queue.pop(0)
                nodes.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                size -= 1
            stack.append(nodes)
        while stack:
            result.append(stack.pop())

        return result

    @staticmethod
    def levelOrderBottom(root: TreeNode) -> List[List[int]]:
        """
        每次插入都在列表头部
        """
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            size = len(queue)
            nodes = []
            while size > 0:
                temp = queue.pop(0)
                nodes.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                size -= 1
            result.insert(0, nodes)

        return result
