# https://leetcode.com/problems/minimum-size-subarray-sum/description/

# 209. Minimum Size Subarray Sum


"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0  # Left pointer
        res = float('inf')  # Track the minimum subarray length
        current_sum = 0  # Initialize the sum of the current window

        for r in range(0,len(nums)):  # Right pointer iterates through the array
            current_sum += nums[r]  # Expand the window by adding nums[r]

            # Shrink the window from the left while the sum is >= target
            while current_sum >= target:
                res = min(res, r - l + 1)  # Update the result
                current_sum -= nums[l]  # Shrink the window from the left
                l += 1

        # Return the result or 0 if no subarray meets the condition
        return 0 if res == float('inf') else res


                    