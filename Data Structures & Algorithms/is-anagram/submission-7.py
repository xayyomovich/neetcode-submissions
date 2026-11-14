class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}

        for i, u in zip(s, t):
            res1 = s.count(i)
            dic1[i] = res1
            res2 = t.count(u)
            dic2[u] = res2

        if dic1 == dic2:
            return True
        else:   
            return False