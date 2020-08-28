#!/usr/bin/python
# -*- encoding: utf-8 -*-
from typing import List

from tree import TreeNode


# 二叉树的层序遍历
class Solution:
    @staticmethod
    def level_order(root: TreeNode) -> List[List[int]]:
        """
        二叉树层序遍历
        """
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            size = len(queue)
            level_nodes = []
            while size > 0:
                temp = queue.pop(0)
                level_nodes.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                size -= 1
            result.append(level_nodes)
        return result
