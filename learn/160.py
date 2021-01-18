#!/usr/bin/python
# -*- encoding: utf-8 -*-


# 找出两个单链表相交的起始节点
class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        先求出两个链表的长度，使用双指针来判断，长链表的指针先移动到相等的长度
        时间复杂度O(n), 空间复杂度：O(1)
        """
        lengthA = self.getLength(headA)
        lengthB = self.getLength(headB)
        sub = abs(lengthA - lengthB)
        slow, fast = headA, headB
        if lengthA > lengthB:
            slow, fast = fast, slow
        while sub:
            fast = fast.next
            sub -= 1
        while slow:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next

        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        使用双指针消除长度差，不需要先求出长度差
        """
        slow, fast = headA, headB
        flag = 0
        while slow and fast:
            if slow == fast:
                return slow
            slow, fast = slow.next, fast.next
            if flag < 3 and not slow:
                slow = headB
                flag += 1
            if flag < 3 and not fast:
                fast = headA
                flag += 1

        return None

    def getLength(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length


if __name__ == '__main__':
    headA = ListNode()
    listA = [4, 1, 8, 4, 5]
    listB = [5, 0, 1, 8, 4, 5]