def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    length = len(s)
    if length == 0:
        return 0
    maxnum = 0
    tmp = 0
    flag = 0
    for i in xrange(1,length):
        for j in xrange(i-1, flag-1, -1):
            if s[i] != s[j]:
                tmp = i - j + 1
                if tmp > maxnum:
                    maxnum = tmp
                print "i=%d j=%d tmp=%d" %(i,j,tmp)
            else:
                flag = j + 1
                if tmp > maxnum:
                    maxnum = tmp
                break
    if maxnum == 0:
        return 1
    else:
        return maxnum

s = "abcabcbb"

num = lengthOfLongestSubstring(s)
print num
