class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        maxsum=arr[0]
        mw=0
        mwo=arr[0]
        for i in range(1,len(arr)):
            mw=max(mwo,mw+arr[i])
            mwo=max(mwo+arr[i],arr[i])
            maxsum=max(maxsum,mwo,mw)
        return maxsum

        