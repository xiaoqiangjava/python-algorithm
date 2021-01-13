#!/usr/bin/python
# -*- encoding: utf-8 -*-


# 两数相加：给定两个非空链表，表示两个非负整数，每位数字都是按照逆序方式存储，并且每个节点只能存储一位数字
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        使用字符串拼接的方式来实现
        """
        x = y = ''
        while l1 or l2:
            if l1:
                x = x + str(l1.val)
                l1 = l1.next
            if l2:
                y = y + str(l2.val)
                l2 = l2.next

        x, y = x[::-1], y[::-1]
        ret = str(int(x) + int(y))[::-1]
        self = head = ListNode(0)
        for c in ret:
            head.next = ListNode(int(c))
            head = head.next

        return self.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        使用初等数学的加法来实现，短的链表高位的值可以用0来代替
        """
        head = self = ListNode(0)
        carry = 0  # 进位，对应位置的两个数相加，超过10进一位
        while carry or l1 or l2:
            val = carry
            if l1:
                l1, val = l1.next, l1.val + val
            if l2:
                l2, val = l2.next, l2.val + val

            carry, val = divmod(val, 10)
            head.next = head = ListNode(val)

        return self.next
