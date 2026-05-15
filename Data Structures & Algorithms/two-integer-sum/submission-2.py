class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        for i, num in enumerate(nums):
            j = target - num
            if j in indexMap:
                return [indexMap[j], i]
            else:
                indexMap[num] = i
        
                
            



        