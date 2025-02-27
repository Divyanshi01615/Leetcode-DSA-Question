class Solution(object):
    def containsDuplicate(self, nums):
        set1=set(nums)
        if len(nums)==len(set1):
            return False
        else:
            return True
        """
        :type nums: List[int]
        :rtype: bool
        """
        