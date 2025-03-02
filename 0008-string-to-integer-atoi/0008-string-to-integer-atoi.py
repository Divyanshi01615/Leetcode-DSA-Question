class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        res=""
        for i in s:
            if not res and i in "+-":
                res+=i
            elif i.isdigit():
                res+=i
            else:
                break
        if res in ["","+","-"]:
            return 0
        n=int(res)
        return max((-2**31),min((2**31-1),n))




        
        