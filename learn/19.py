#!/usr/bin/python
# -*- encoding: utf-8 -*-


# 删除链表的倒数第n个节点
class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution(object):
    def removeNthFromEnd_1(self, head: ListNode, n: int) -> ListNode:
        """
        brute force：指针每移动一次，判断当前元素是否是倒数第n个元素
        """
        if not head:
            return head
        dummy, dummy.next = ListNode(), head
        cur = dummy
        while cur:
            fast = cur
            x = n
            while x:
                fast = fast.next
                x = x - 1
            if not fast or not fast.next:
                cur.next.next, cur.next = None, cur.next.next
                return dummy.next
            cur = cur.next
        return None

    def removeNthFromEnd_2(self, head: ListNode, n: int) -> ListNode:
        """
        先计算链表的长度l，然后再次遍历删除l-n的下一个元素
        """
        dummy, dummy.next = ListNode(), head
        cur = dummy
        for idx in range(self.getLength(head) - n):
            cur = cur.next
        cur.next.next, cur.next = None, cur.next.next
        return dummy.next

    def removeNthFromEnd_3(self, head: ListNode, n: int) -> ListNode:
        """
        使用栈数据结构来实现
        """
        dummy, dummy.next = ListNode(), head
        cur = dummy
        stack = list()
        while cur:
            stack.append(cur)
            cur = cur.next

        while n:
            stack.pop()
            n -= 1
        top = stack.pop()
        top.next.next, top.next = None, top.next.next

        return dummy.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        使用双指针来实现，fast指针比slow指针先走n步，当fast达到链表的末尾时，删除slow的下一个节点
        """
        dummy, dummy.next = ListNode(), head
        slow, fast = dummy, head
        for idx in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        slow.next.next, slow.next = None, slow.next.next

        return dummy.next


    def getLength(self, head: ListNode) -> int:
        """
        计算链表的长度
        """
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        return length


if __name__ == '__main__':
    solution = Solution()
    h = ListNode(1)
    h.next = ListNode(2)
    solution.removeNthFromEnd(h, 1)
