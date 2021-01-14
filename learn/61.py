#!/usr/bin/python
# -*- encoding: utf-8 -*-


# 旋转链表：给定一个链表，旋转链表，将链表的每个节点向右移动k个位置，其中k是非负数
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        使用双指针来实现
        """
        if not head or not head.next:
            return head
        # 先获取链表的长度，如果k大于链表的长度，取模
        length = self.getLength(head)
        k = k % length
        if not k:
            return head
        # 定义两个指针，fast指针比slow指针先走k步
        dummy, dummy.next = ListNode(), head
        fast = slow = dummy
        while k:
            fast = fast.next
            k -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        # slow.next为新的头接地那，slow的下一个节点指向None，fast的下一个节点指向原链表的头结点
        slow.next, fast.next, dummy.next = None, dummy.next, slow.next

        return dummy.next

    def getLength(self, head: ListNode) -> int:
        length = 0
        while head:
            head = head.next
            length += 1

        return length

