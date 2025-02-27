class Solution(object):
    def twoSum(self, nums, target):
        res=[]
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    res.append(i)
                    res.append(j)
                    break
        return res

        