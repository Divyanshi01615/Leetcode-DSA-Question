class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1=set()
        j=0
        maxlen=0
        for i in range(len(s)):
            while s[i] in s1:
                s1.remove(s[j])
                j+=1
            s1.add(s[i])
            maxlen=max(maxlen,i-j+1)
        return maxlen