# https://leetcode.com/problems/longest-consecutive-sequence/description/

# 128. Longest Consecutive Sequence

'''

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0;
        numsSet = set(nums)
        if len(nums) == 0:
            return 0
        for v in nums:
            tempRes = 1
            if v-1 in numsSet:
                continue
            while v+1 in numsSet:
                tempRes = tempRes+1
                v = v+1        
            if tempRes > res:
                res = tempRes
        return res




        
