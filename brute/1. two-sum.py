from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = target
        for i in range (len(nums)):
            temp = temp-nums[i]
            
            for j in range (i+1, len(nums)):
                if temp == nums[j] and (i != j):
                    return [i,j]
            temp = target


