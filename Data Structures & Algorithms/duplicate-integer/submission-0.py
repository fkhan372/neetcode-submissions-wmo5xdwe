class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if (nums[y] == nums[x]):
                    return True
                else:
                    continue
        return False
