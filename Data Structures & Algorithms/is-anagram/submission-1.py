class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs = {}
        ct = {}

        for i in s:
            if i in cs:
                cs[i] += 1
            else:
                cs[i] = 1
        for i in t:
            if i in ct:
                ct[i] += 1
            else:
                ct[i] = 1
        
        if cs == ct:
            return True
        else:
            return False