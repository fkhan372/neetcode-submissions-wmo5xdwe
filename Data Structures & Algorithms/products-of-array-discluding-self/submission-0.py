class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        counter = 0

        while (counter < len(nums)):
            copiedList = nums.copy()
            copiedList[counter] = 1
            output[counter] = math.prod(copiedList)
            counter += 1

        return output