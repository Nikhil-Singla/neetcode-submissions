class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for index, element in enumerate(nums):
            key = target - element
            
            if key not in dict:
                dict[element] = index
            else:
                return [dict[key], index]

        return [0, 0]