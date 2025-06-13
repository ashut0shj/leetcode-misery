#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums = (sorted(nums))
        res = []
        for i in range (len(nums) - 1):
            res.append(nums[i+1] - nums[i])

        count , max_c = 0, 0
        for i in res:
            if i == 1:
                count = count+1
            else:
                if max_c < count :
                    max_c = count
                count = 0
        
        if max_c < count :
            max_c = count

        return max_c + 1
# @lc code=end

