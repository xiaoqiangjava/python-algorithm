#!/usr/bin/python
# -*- encoding: utf-8 -*-


# 翻转给定区间的链表，区间之外的链表保持顺序不变
class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution(object):
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        使用迭代，记录开始节点的前继节点pre，将m到n节点翻转之后，调整pre的next指针
        """
        if m == n:
            return head
        dummy, dummy.next = ListNode(), head
        start_pre, cur, pre = None, dummy, None
        length = 0
        while cur:
            if length + 1 == m:
                start_pre = cur
            if m <= length < n:
                cur.next, pre, cur = pre, cur, cur.next
            elif length == n:
                start_pre.next.next, start_pre.next, cur.next = cur.next, cur, pre
                if m == 1:  # 对于m等于1的情况特殊处理
                    dummy.next = cur
                break
            else:
                cur = cur.next
            length += 1

        return dummy.next


if __name__ == '__main__':
    nodes = [1, 2, 3, 4, 5]
    d = h = ListNode()
    for node in nodes:
        h.next = ListNode(node)
        h = h.next
    solution = Solution()
    result = solution.reverseBetween(d.next, 1, 3)

