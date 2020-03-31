class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1;
        first, second = 1, 1
        for _ in range(2, n + 1):
            first, second = second, first + second

        return second
