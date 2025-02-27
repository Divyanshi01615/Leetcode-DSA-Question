class Solution(object):
    def isPalindrome(self, s):
        l=0
        h=len(s)-1
        while l<h:
            while l<h and not s[l].isalnum():
                l+=1
            while l<h and not s[h].isalnum():
                h-=1
            if s[l].lower()!=s[h].lower():
                return False
            l+=1
            h-=1
        return True

        