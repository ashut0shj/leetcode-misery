#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums:
            hash[i] = 1 + hash.get(i, 0)
        
        return sorted(hash, key = hash.get, reverse = True)[:k]

        
        
# @lc code=end

