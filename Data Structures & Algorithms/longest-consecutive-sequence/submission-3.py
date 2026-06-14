class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSeq = 1
        currentSeq = 1
        i = 0
        hashSet = set(nums)

        if (len(nums) == 0):
            return 0

        while (i < len(nums)):
            if ((nums[i] - 1) in hashSet):
                i += 1
                currentSeq = 1
            elif ((nums[i] + currentSeq) in hashSet):
                currentSeq += 1
                if currentSeq > longestSeq:
                    longestSeq = currentSeq
            else:
                i += 1
                currentSeq = 1
            
        return longestSeq