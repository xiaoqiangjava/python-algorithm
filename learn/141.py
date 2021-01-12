#!/usr/bin/python
# -*- encoding: utf-8 -*-


# 判断一个链表是否有环
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle_1(self, head: ListNode) -> bool:
        """
        使用一个set来存储已经遍历过的节点，看是否在set中存在后面的节点
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        nodes = set()
        while head:
            if head in nodes:
                return True
            nodes.add(head)
            head = head.next
        return False

    def hasCycle(self, head: ListNode) -> bool:
        """
        使用快慢指针：快指针走一步，慢指针走两步，如果两个指针能够相遇，那么这个链表有环
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        fast, slow = head, head
        while fast:
            slow = slow.next
            if not fast.next:
                return False
            fast = fast.next.next

            if fast == slow:
                return True

        return False
