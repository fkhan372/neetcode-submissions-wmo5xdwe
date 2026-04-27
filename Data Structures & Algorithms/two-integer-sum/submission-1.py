class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        returnArray = []
        for x in range(len(nums)):
            numToFind = target - nums[x]
            if numToFind == nums[x] and nums.count(numToFind) >= 2:
                returnArray = [i for i, x in enumerate(nums) if x == numToFind]
                return returnArray[0:2]
            elif numToFind in nums and nums.index(numToFind) != x:
                returnArray = [x, nums.index(numToFind)]
                return returnArray
