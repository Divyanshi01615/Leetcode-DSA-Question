class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum=0
        msum=nums[0]
        for i in range(len(nums)):
            csum+=nums[i]
            msum=max(csum,msum)
            if csum<0:
                csum=0
        return msum
        


        