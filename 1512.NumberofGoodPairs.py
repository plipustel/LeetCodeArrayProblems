
# 
# @PROBLEM       : 1512. Number of Good Pairs
# @LEVEL         : EASY
# @STATUS        : SOLVED !
# @COMPLEXITY    : O(n^2)
# @SOLVED BY     : PLIPUS TELAUMBANUA <www.plipustel.com>
# @LEETCODE      : https://leetcode.com/u/plipustel/
# @DATE          : SATURDAY, JUN 22 2024
#
# @PROBELM SOURCE: www.leetcode.com <https://leetcode.com/problems/number-of-good-pairs/description/>
# @PROBLEM DESC  :
# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
# Example 1:
#   Input: nums = [1,2,3,1,1,3]
#   Output: 4
#   Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
#                   
# Example 2:
#   Input: nums = [1,1,1,1]
#   Output: 6
#   Explanation: Each pair in the array are good.

# Example 3:
#   Input: nums = [1,2,3]
#   Output: 0
#  
# Constraints:
#   1 <= nums.length <= 100
#   1 <= nums[i] <= 100
#   Seen this question in a real interview before?
#   1/5

 
class Solution(object):
    def __init__(self):
        self.arr = []
        
    def numIdenticalPairs(self, nums):
        return self._buildArray(nums, 0)
    
    def _buildArray(self, nums, start):
        if start >= len(nums):
            return 
        for r in range(start, (len(nums) - 1)):
           if ((nums[start] == nums[r+1]) and (r < r+1)):
               # print(f'({start}, {r+1}):{nums[start]}, {nums[r+1]}')
                self.arr.append((nums[start], nums[r+1]))

        self._buildArray(nums, start + 1)
        return len(self.arr)
        
# Test: case1 = [1,2,3,1,1,3], case 2 = [1,1,1,1], case 3 = [1,2,3]    
nums = [1,2,3,1,1,3]
sol = Solution()
print(sol.numIdenticalPairs(nums))
