class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i, n in enumerate(nums):
            temp = target - n
            if temp in hash:
                return [hash[temp], i]
            hash[n] = i

            