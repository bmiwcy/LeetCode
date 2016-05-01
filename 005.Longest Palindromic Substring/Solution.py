
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in xrange(len(s)):
            for j in xrange(2):
                tmp = self.helper(s,i,i+j)
                if tmp>res:
                    res = tmp
        return res
        

    def helper(self, s, l, r):
        while l>=0 and r<len(s) and s[l]== s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
print "hi"
