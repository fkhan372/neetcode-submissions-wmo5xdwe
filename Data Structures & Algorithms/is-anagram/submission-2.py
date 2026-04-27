class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        sortedS = "".join(sorted(s))
        sortedT = "".join(sorted(t))

        for x in range(len(s)):
            if sortedS[x] != sortedT[x]:
                return False
            else:
                continue
        return True