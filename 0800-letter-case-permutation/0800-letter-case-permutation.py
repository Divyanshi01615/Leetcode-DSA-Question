class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def rec(i,path):
            if i==len(s):
                res.append("".join(path))
                return
            if s[i].isalpha():
                path.append(s[i].lower())
                rec(i+1,path)
                path.pop()
                path.append(s[i].upper())
                rec(i+1,path)
                path.pop()
            else:
                path.append(s[i])
                rec(i+1,path)
                path.pop()
        res=[]
        rec(0,[])
        return res

        