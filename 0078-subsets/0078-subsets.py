class Solution:
        def subsets(self, nums: List[int]) -> List[List[int]]:
            res = []
            op = []
            self.solve(nums, 0, op, res)
            return res
        
        def solve(self, nums: List[int], start: int, op: List[int], res: List[List[int]]):
            if start == len(nums):
                res.append(op.copy())
                return
            
            self.solve(nums, start + 1, op, res)
            op.append(nums[start])
            self.solve(nums, start + 1, op, res)
            op.pop()
    
        