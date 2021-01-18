#!/usr/bin/python
# -*- encoding: utf-8 -*-
import math


# 回文链表
class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution(object):
    def isPalindrome(self, head: ListNode) -> bool:
        """
        使用列表存储节点的值
        时间复杂度O(n), 空间复杂度：O(n)
        """
        values = []
        while head:
            values.append(head.val)
            head = head.next

        return values == values[::-1]

    def isPalindrome(self, head: ListNode) -> bool:
        """
        将节点后半部分翻转，然后通过双指针来实现
        时间复杂度：O(n), 空间复杂度：O(1)
        """
        length = self.getLength(head)
        if length == 1:
            return True
        if length == 2:
            return head.val == head.next.val
        if length == 3:
            return head.val == head.next.next.val
        mid, temp = math.ceil(length / 2), 1
        cur = head
        while head:
            temp += 1
            head = head.next
            if temp == mid:
                head.next = self.reverseList(head)
                break
        while head and head.next:
            if cur.val != head.next.val:
                return False
            cur, head = cur.next, head.next
        return True

    def reverseList(self, head):
        cur = head.next
        pre = None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre

    def getLength(self, head: ListNode) -> int:
        length = 0
        while head:
            head = head.next
            length += 1

        return length


if __name__ == '__main__':
    nodes = [1, 2, 2, 1]
    h = cur = ListNode()
    for node in nodes:
        cur.next = ListNode(node)
        cur = cur.next
    solution = Solution()
    solution.isPalindrome(h.next)
