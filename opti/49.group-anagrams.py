#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from typing import List
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        s=[]
        
        for i in range (len(strs)):
            s.append(''.join(sorted(strs[i])))
            
        s=set(s)
        res = [[] for _ in range ( len(s))]

        for i, n in enumerate(s):
            hash[n] = i
        
        for i in strs:
            res[hash[''.join(sorted(i))]].append(i)

        return res
        






# @lc code=end

