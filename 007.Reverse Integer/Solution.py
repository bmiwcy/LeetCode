class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2147483648
        val = 0
        tmp = 0
        if x<0:
            tmp = x
            x = -tmp
        val = val*10 + x%10
        x = x/10
        while x:
            val = val*10 + x%10
            x = x/10
        if val>INT_MAX:
            return 0
        if tmp<0:
            return -val
        return val
