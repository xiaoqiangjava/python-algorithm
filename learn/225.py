#!/usr/bin/python
# -*- encoding: utf-8 -*-


# 用对列实现栈
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_queue = []
        self.out_queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.in_queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while self.in_queue:
            e = self.in_queue.pop(0)
            if not self.in_queue:
                self.in_queue, self.out_queue = self.out_queue, self.in_queue
                return e
            else:
                self.out_queue.append(e)
        return None

    def top(self) -> int:
        """
        Get the top element.
        """
        while self.in_queue:
            e = self.in_queue.pop(0)
            self.out_queue.append(e)
            if not self.in_queue:
                self.in_queue, self.out_queue = self.out_queue, self.in_queue
                return e
        return None

    def empty(self) -> bool:
        """
        Return whether the stack is empty.
        """
        return not self.in_queue


if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    print(obj.top())
    print(obj.pop())
    print(obj.empty())
