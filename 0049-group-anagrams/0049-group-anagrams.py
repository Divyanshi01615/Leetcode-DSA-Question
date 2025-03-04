class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for i in strs:
            sw="".join(sorted(i))
            dic[sw].append(i)
        return list(dic.values())
        

        