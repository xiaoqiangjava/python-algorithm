#!/usr/bin/python
# -*- encoding: utf-8 -*-


# 无重复字符的最长子串
def length_of_longest_substring(s: str) -> int:
    """
    滑动窗口
    """
    if not s:
        return 0
    window = set()  # 窗口
    max_len = 0  # 记录最大长度
    left = 0  # 记录最左边的下标
    for i in range(len(s)):
        while s[i] in window:
            window.remove(s[left])
            left += 1
        window.add(s[i])
        max_len = max(max_len, len(window))

    return max_len


if __name__ == '__main__':
    print(length_of_longest_substring('abcabcbb'))
