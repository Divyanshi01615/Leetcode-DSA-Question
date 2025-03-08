class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        n=len(arr)
        res=[1]*n
        lp=1
        for i in range(n):
            res[i]=lp
            lp*=arr[i]
        rp=1
        for i in range(n-1,-1,-1):
            res[i]*=rp
            rp*=arr[i]
        return res

            
           
                    

           

        