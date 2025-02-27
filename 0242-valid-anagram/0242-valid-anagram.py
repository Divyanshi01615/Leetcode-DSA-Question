class Solution(object):
    def isAnagram(self, s, t):
        s1=list(s)
        t1=list(t)
        s1.sort()
        t1.sort()
        for i,j in zip(s1,t1):
            if s1!=t1:
                return False
        return True
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        