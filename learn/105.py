#!/usr/bin/python
# -*- encoding: utf-8 -*-
from typing import List
from tree import TreeNode


# 前序与中序遍历序列构造二叉树
class Solution:
    def buildTree(self, pre_order: List[int], in_order: List[int]) -> TreeNode:
        """
        递归实现: 前序遍历的第一个节点是根节点，由于不存在重复元素，因此可以找到根节点在中序遍历中的位置，该位置
        可以将中序遍历的列表分隔成两部分，前半部分是整个树的左子树，后半部分是整个树的右子树；
        前序遍历中第一个元素后面取中序遍历前半部分的长度为整个树的左子树，剩下的部分为整个树的右子树
        按照这个思路递归，直到中序和前序遍历的列表为空，返回None
        """
        if not (pre_order and in_order):
            return None
        # 根节点为前序遍历的第一个元素
        root = TreeNode.TreeNode(pre_order[0])
        # 找到根节点在中序遍历中的位置
        root_idx = in_order.index(pre_order[0])
        # 递归构建左子树
        root.left = self.buildTree(pre_order[1:root_idx + 1], in_order[:root_idx + 1])
        # 递归的构建右子树
        root.right = self.buildTree(pre_order[root_idx + 1:], in_order[root_idx + 1:])

        return root


if __name__ == '__main__':
    solution = Solution()
    tree = solution.buildTree([6, 2, 1, 4, 3, 5, 7, 9, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(tree)
