#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = ''
        for i in s:
            for j in i :
                for k in j:
                    if k.isalpha():
                        l = l + k.lower()
        print(l)

        for i in range ((len(l)//2) + 1):
            if l[i] != l[-1-i]:
                return False
        return True
# @lc code=end

