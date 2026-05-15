class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap, tMap = {}, {}
        for sl, tl in zip(s, t):
            if sl not in sMap:
                sMap[sl] = 1
            else:
                sMap[sl] += 1
            if tl not in tMap:
                tMap[tl] = 1
            else:
                tMap[tl] += 1
        return sMap == tMap