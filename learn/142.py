#!/usr/bin/python
# -*- encoding: utf-8 -*-


# 返回链表入环的第一个节点
class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution(object):
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        使用set来存储元素, 空间复杂度O(n)
        """
        nodes = set()
        while head:
            if head in nodes:
                return head
            nodes.add(head)
            head = head.next

        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        """
        
        """