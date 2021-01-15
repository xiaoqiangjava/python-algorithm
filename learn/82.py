#!/usr/bin/python
# -*- encoding: utf-8 -*-


# 删除链表中的重复元素，只保留原始链表中没有重复出现的数字
class ListNode(object):
    def __init__(self, val = 0):
        self.val = val
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        使用双指针来实现
        """
        dummy, dummy.next = ListNode(), head
        pre = dummy
        while head and head.next:
            flag = False
            while head and head.next:     # 循环删除所有重复的元素
                if head.val == head.next.val:
                    flag = True
                    head.next.next, head.next = None, head.next.next
                elif flag:  # 如果当前head是重复元素，跳出循环，删除当前元素
                    break
                else:
                    pre, head = head, head.next
                    break
            if flag:    # 如果存在重复元素，删除head指针所在的元素，head向后移动
                pre.next.next, pre.next, head = None, pre.next.next, head.next

        return dummy.next


if __name__ == '__main__':
    h = ListNode()
    nodes = [1, 2, 3, 3, 4, 4, 5]
    cur = h
    for node in nodes:
        cur.next = ListNode(node)
        cur = cur.next

    solution = Solution()
    solution.deleteDuplicates(h.next)
