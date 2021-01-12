#!/usr/bin/python
# -*- encoding: utf-8 -*-


# 有效的括号：给定一个只包含括号的字符串，判断字符串是否有效：1. 左括号必须用相同类型的右括号闭合 2. 左括号必须正确的顺序闭合
class Solution(object):
    def isValid(self, s: str) -> bool:
        """
        使用栈数据结构来实现，map记录匹配的括号，当出现左括号时，直接入栈，出现右括号时，判断栈顶的括号是否匹配
        """
        if len(s) & 1 == 1:
            return False

        stack = list()
        pairs = {')': '(', ']': '[', '}': '{'}  # 使用map存储，目的是为了通过右括号查询到匹配的做括号
        for c in s:
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)

        return not stack

    def isValid_1(self, s: str) -> bool:
        """
        第一版代码，简单的思考，没有使用map存储括号对
        """
        if len(s) & 1 == 1:
            return False
        stack = list()
        left = '({['
        for c in s:
            if c in left:
                stack.append(c)  # 如果是左括号，入栈
            else:
                if not stack:   # 右括号时，栈中必须要有括号，否则不合法
                    return False
                top = stack.pop()
                if c == ')' and top == '(':
                    pass
                elif c == ']' and top == '[':
                    pass
                elif c == '}' and top == '{':
                    pass
                else:
                    return False

        return not stack
