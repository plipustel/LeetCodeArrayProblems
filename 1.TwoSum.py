
# 
# @PROBLEM       : 1. TWO SUM
# @LEVEL         : EASY
# @STATUS        : SOLVED !
# @COMPLEXITY    : O(n)
# @SOLVED BY     : PLIPUS TELAUMBANUA <www.plipustel.com>
# @LEETCODE      : https://leetcode.com/u/plipustel/
# @DATE          : SATURDAY, JUN 22 2024
#
# @PROBLEM SOURCE: www.leetcode.com <https://leetcode.com/problems/two-sum/description/>
# @PROBLEM DESC  :
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].\
    
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
 
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

class Solution(object):
    def twoSum(self, nums, target):
        # creating hash table
        hash_table = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in hash_table:
                return [hash_table[complement], i]
            else:
                hash_table[nums[i]] = i


# case1: nums = [2,7,11,15], target = 9, output: [0,1]
# case2: nums = [3,2,4], target = 6, output: [1,2]
# case3: nums = [3,3], target = 6, output: [0,1]
sol = Solution()
print(sol.twoSum([2,7,11,15], 9))