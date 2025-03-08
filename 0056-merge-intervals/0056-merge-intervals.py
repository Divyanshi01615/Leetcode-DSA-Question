class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        i=0
        arr.sort()
        for j in range(1,len(arr)):
            if arr[i][1]>=arr[j][0]:
                arr[i][1]=max(arr[i][1],arr[j][1])
            else:
                i+=1
                arr[i]=arr[j]
        return arr[:i+1]

        