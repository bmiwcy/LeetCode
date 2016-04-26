class Solution(object):
  def twoSum(self, nums, target):
    length = len(nums)
    for i in xrange(0, length-1):
      for j in xrange(0, length):
        if (target == nums[i]+nums[j]):
          return i,j
