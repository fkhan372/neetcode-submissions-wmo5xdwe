class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mainList = []
        subList = []
            
        if (int(len(strs)) == 0):
            return mainList

        while (strs):
            subList.append(strs[0])
            firstSorted = "".join(sorted(strs[0]))
            for x in range(1, len(strs)):
                secondSorted = "".join(sorted(strs[x]))
                if firstSorted == secondSorted:
                    subList.append(strs[x])

            mainList.append(subList.copy())
            for y in subList:
                strs.remove(y)
            subList.clear()

        return mainList