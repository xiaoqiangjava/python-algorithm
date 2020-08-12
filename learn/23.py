#!/usr/bin/python
# -*- encoding: utf-8 -*-
import heapq
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        """
        :type val: int
        :type next: ListNode
        """
        self.val = val
        self.next = next

    def __str__(self):
        res = str(self.val)
        while self.next:
            res = f"%s -> %s" % (res, self.next.val)
            self.next = self.next.next
        return res


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        queue = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(queue, (lists[i].val, i))

        dummy = ListNode(0)
        pre = dummy
        while queue:
            val, idx = heapq.heappop(queue)
            pre.next = lists[idx]
            lists[idx] = lists[idx].next
            pre = pre.next
            if pre.next:
                heapq.heappush(queue, (pre.next.val, idx))

        return dummy.next


if __name__ == '__main__':
    nodes = []
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(7)
    nodes.append(l1)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(5)
    nodes.append(l2)

    solution = Solution()
    res = solution.mergeKLists(nodes)
    print(res)
