class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        tList = list(t)
        for x in range(len(s)):
            for y in range(len(tList)):
                if (s[x] == tList[y]):
                    tList.pop(y)
                    break
            if len(s) == len(tList):
                return False

        if not tList:
            return True
        else:
            return False