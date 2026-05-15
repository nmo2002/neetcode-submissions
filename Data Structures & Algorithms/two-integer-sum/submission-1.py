class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i in range(len(nums)):
            if nums[i] not in prevMap:
                prevMap[nums[i]] = i
            j = target - nums[i]
            if j in prevMap and prevMap[j] != i:
                return [prevMap[j], i]


        