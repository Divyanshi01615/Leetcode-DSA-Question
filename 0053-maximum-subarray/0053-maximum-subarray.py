class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=nums[0]
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            if(s>maxi):
                maxi=s
            if(s<0):
                s=0
        return maxi

        