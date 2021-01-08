#!/usr/bin/python
# -*- encoding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 链表的反转
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        迭代解法：遍历整个链表，将当前节点与其下一个节点断开连接，每个节点都将指针指向其前一个节点，由于head
        没有前继节点，可以先申明一个None节点作为前继节点
        1 -> 2 -> 3 -> 4 -> None
        """
        # 定义一个前继节点，初始值为None,随着链表的反转，前继节点随着变化
        prev = None
        while head:
            temp = head.next    # 记录当前节点的下一个节点
            head.next = prev    # 将头结点与其next节点断开，将head的next指针指向prov节点
            prev = head         # prov指针指向head
            head = temp

        return prev

    def reverseList_1(self, head: ListNode) -> ListNode:
        """
        使用Python语言简写
        """
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next

        return prev

    def reverseList_2(self, head: ListNode) -> ListNode:
        """
        递归实现
        """
        if not head or not head.next:
            return head
        ret = self.reverseList_2(head.next)  # 这里得到的是原链表的最后一个节点，也就是发转之后链表的头节点
        head.next.next = head
        head.next = None

        return ret
