from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() 
        self.solve(nums, 0, [], res)
        return res

    def solve(self, nums: List[int], start: int, op: List[int], res: List[List[int]]):
        res.append(op.copy())
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue 
            op.append(nums[i])
            self.solve(nums, i + 1, op, res)
            op.pop()
