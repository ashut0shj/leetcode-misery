#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r , l = 0, len(numbers) -1

        for i in range(len(numbers)):
            sum = numbers[r] + numbers[l]
            if sum > target:
                l -= 1
            elif sum < target:
                r += 1
            else:
                return [r+1, l+1]
                
       

            
        
# @lc code=end

