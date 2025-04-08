class Solution:
    def rob(self, nums: List[int]) -> int:
        s1=0
        s2=0
        for i in range(0,len(nums)):
            t=max(s1,s2+nums[i])
            s2,s1=s1,t
        return s1

        