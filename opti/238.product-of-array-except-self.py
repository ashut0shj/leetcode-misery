#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range (len(nums))]
        temp = 1
        for i in range (1, len(nums)):
            temp = temp * nums[i-1]
            res[i] = temp
        
        temp = 1
        for i in range (len(nums) -2 , -1, -1):
            temp = temp * nums[i+1]
            res[i] = res[i] * temp
        return (res)
        
# @lc code=end

