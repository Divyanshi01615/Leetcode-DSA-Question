class Solution(object):
    def findDisappearedNumbers(self, nums):
        n=len(nums)
        missing_numbers=list()
        dic={}
        for i in range(1, n + 1):
            dic[i] = 0
        for num in nums:
            dic[num] += 1
        for i, j in dic.items():
            if j == 0:
                missing_numbers.append(i)
        return missing_numbers
        