# @PROBLEM       : 2125. Number of Laser Beams in a Bank
# @LEVEL         : MEDIUM
# @STATUS        : SOLVED !
# @COMPLEXITY    : O(n^2)
# @SOLVED BY     : PLIPUS TELAUMBANUA <www.plipustel.com>
# @LEETCODE      : https://leetcode.com/u/plipustel/
# @DATE          : TUESDAY, JUN 25 2024
#
# @PROBELM SOURCE: https://leetcode.com/problems/largest-local-values-in-a-matrix/description/
# @PROBLEM DESC  :
# Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary 
# string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] 
# represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' 
# means the cell has a security device.
# There is one laser beam between any two security devices if both conditions are met:
# The two devices are located on two different rows: r1 and r2, where r1 < r2.
# For each row i where r1 < i < r2, there are no security devices in the ith row.
# Laser beams are independent, i.e., one beam does not interfere nor join with another.

# Input: bank = ["011001","000000","010100","001000"]
# Output: 8
# Explanation: Between each of the following device pairs, there is one beam. In total, there are 8 beams:
#  * bank[0][1] -- bank[2][1]
#  * bank[0][1] -- bank[2][3]
#  * bank[0][2] -- bank[2][1]
#  * bank[0][2] -- bank[2][3]
#  * bank[0][5] -- bank[2][1]
#  * bank[0][5] -- bank[2][3]
#  * bank[2][1] -- bank[3][2]
#  * bank[2][3] -- bank[3][2]
# Note that there is no beam between any device on the 0th row with any on the 3rd row.
# This is because the 2nd row contains security devices, which breaks the second condition.

# Input: bank = ["000","111","000"]
# Output: 0
# Explanation: There does not exist two devices located on two different rows.

# Constraints:

# m == bank.length
# n == bank[i].length
# 1 <= m, n <= 500
# bank[i][j] is either '0' or '1'.

class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        device_counts = [row.count('1') for row in bank if row.count('1') > 0]      
             
        total_beams = 0

        for i in range(len(device_counts) - 1):
            print(device_counts[i], device_counts[i+1])
            total_beams = total_beams + device_counts[i] * device_counts[i + 1]
           
        return total_beams
              
# input1: 
bank = ["011001","000000","010100","001000"]

# input2: bank = ["000","111","000"]

sol = Solution()
print(sol.numberOfBeams(bank))