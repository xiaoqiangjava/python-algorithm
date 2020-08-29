#!/usr/bin/python
# -*- encoding: utf-8 -*-
from typing import List
from tree import TreeNode


# 二叉树的锯齿形层次遍历
class Solution:
    @staticmethod
    def zigzagLevelOrder(root: TreeNode) -> List[List[int]]:
        """
        借助队列迭代实现
        """
        if not root:
            return []
        result = []
        queue = [root]
        level = 1
        while queue:
            size = len(queue)
            level_nodes = []
            while size > 0:
                temp = queue.pop(0)
                if level & 1 == 1:
                    level_nodes.append(temp.val)
                else:
                    level_nodes.insert(0, temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                size -= 1
            result.append(level_nodes)
            level += 1
        return result


if __name__ == '__main__':
    node = TreeNode.TreeNode(6)
    node.left = TreeNode.TreeNode(2)
    node.right = TreeNode.TreeNode(7)
    node.left.left = TreeNode.TreeNode(1)
    node.left.right = TreeNode.TreeNode(4)
    node.left.right.left = TreeNode.TreeNode(3)
    node.left.right.right = TreeNode.TreeNode(5)
    node.right.right = TreeNode.TreeNode(9)
    node.right.right.left = TreeNode.TreeNode(8)
    print(Solution.zigzagLevelOrder(node))
