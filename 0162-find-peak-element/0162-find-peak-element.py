class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        n=len(arr)
        if n == 1:
            return 0
        
        if arr[0] > arr[1]:
            return 0
        
        if arr[n - 1] > arr[n - 2]:
            return n - 1
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i]>arr[i+1]:
                return i
        return -1
        
