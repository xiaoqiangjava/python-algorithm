#!/usr/bin/python
# -*- encoding: utf-8 -*-
from typing import List

from tree import TreeNode


# 从中序与后序遍历序列构造二叉树
class Solution:
    def buildTree(self, in_order: List[int], post_order: List[int]) -> TreeNode:
        """
        迭代实现：后序遍历的最后一个元素是树的根节点，该节点在中序遍历的列表中将列表分隔为前后两个部分，前半部分
        列表的值为整个树的左节点，后半部分列表的值为整个树的右节点，而在后序遍历中取中序遍历后半部分的元素个数即
        为当前树的右子树，剩下的为整个树的左子树，按照这个思路递归，即可得到整个树
        """
        # 递归结束条件
        if not (in_order and post_order):
            return None
        # 后序遍历的最后一个节点为整个树的根节点
        root = TreeNode.TreeNode(post_order[-1])
        # 找到根节点在中序遍历中的位置
        root_idx = in_order.index(post_order[-1])
        # 递归构建左子树
        root.left = self.buildTree(in_order[:root_idx], post_order[:root_idx])
        # 递归构建右子树
        root.right = self.buildTree(in_order[root_idx + 1:], post_order[root_idx: -1])

        return root


if __name__ == '__main__':
    solution = Solution()
    tree = solution.buildTree([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 3, 5, 4, 2, 8, 9, 7, 6])
    print(tree)
