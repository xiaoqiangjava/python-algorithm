#!/usr/bin/python
# encoding: utf-8 -*-


# k个一组翻转链表
class ListNode(object):
    def __init__(self, val = 0):
        self.val = val
        self.next = None


class Solution(object):
    def reverseKGroup_1(self, head: ListNode, k: int) -> ListNode:
        """
        使用递归，每k个链表组成一个新的链表进行翻转，翻转之后的next指针指向后面一组链表翻转后的head
        """
        dummy, dummy.next = ListNode(), head
        cur = dummy
        x = k
        while x:
            cur = cur.next
            if not cur:
                return head
            x -= 1
        temp = cur.next
        cur.next = None
        self.reverse(dummy.next)
        head.next = self.reverseKGroup(temp, k)

        return cur

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        迭代实现：空间复杂度优化
        """
        dummy, dummy.next = ListNode(), head
        pre = cur = dummy
        while head:
            for _ in range(k):
                cur = cur.next
                if not cur:
                    pre.next = head
                    return dummy.next
            temp, cur.next = cur.next, None
            pre.next = self.reverse(head)
            head, cur = cur, head   # 由于翻转之后head,cur指针的位置发生变化，所以交换指针的位置保持原来的位置不变
            pre, head, cur.next = cur, temp, temp   # 前面断开了cur与后面的链接，这里将cur.next指向剩余的链表

        return dummy.next

    @staticmethod
    def reverse(head: ListNode) -> ListNode:
        """
        翻转链表
        """
        prev, cur = None, head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        return prev


if __name__ == '__main__':
    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    h.next.next.next = ListNode(4)
    h.next.next.next.next = ListNode(5)
    solution = Solution()
    result = solution.reverseKGroup(h, 2)
