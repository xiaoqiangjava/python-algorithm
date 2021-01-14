#!/usr/bin/python
# -*- encoding: utf-8 -*-


# 删除排序链表中的重复元素
class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        迭代实现，如果当前节点与下一个节点的值相等则删除下一个节点
        需要注意的是指针移动时，如果下一个元素重复，则删除下一个元素，指针不需要移动
        """
        cur = head
        while cur or cur.next:
            if cur.val == cur.next.val:
                cur.next.next, cur.next = None, cur.next.next
            else:
                cur = cur.next

        return head
