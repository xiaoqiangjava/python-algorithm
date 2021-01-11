#!/usr/bin/python
# -*- encoding: utf-8 -*-


# 两两交换链表中的节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        递归实现
        """
        if not head or not head.next:
            return head

        ret = head.next
        head.next = self.swapPairs(head.next.next)
        ret.next = head
        return ret

    def swapPairs_1(self, head: ListNode) -> ListNode:
        """
        迭代实现
        """
        dummy, dummy.next = self, head
        while dummy.next and dummy.next.next:
            node1 = dummy.next
            node2 = dummy.next.next
            dummy.next, node1.next, node2.next = node2, node2.next, node1
            dummy = node1

        return self.next
