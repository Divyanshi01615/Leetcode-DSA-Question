class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(0,len(nums)):
            if target not in nums:
                return -1
            else:
                if nums[i]==target:
                    return i
                
        