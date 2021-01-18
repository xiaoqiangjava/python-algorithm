#!/usr/bin/python
# -*- encoding: utf-8 -*-


# 删除链表中等于给定值的所有节点
class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution(object):
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy, dummy.next = ListNode(), head
        pre = dummy
        while head:
            if head.val == val:
                pre.next, head.next, head = head.next, None, head.next
            else:
                pre, head = head, head.next

        return dummy.next
