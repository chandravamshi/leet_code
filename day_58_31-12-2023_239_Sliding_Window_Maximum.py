# https://leetcode.com/problems/sliding-window-maximum/description/

# 239. Sliding Window Maximum

'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque() # store the indexes
        l = r = 0
        
        while r < len(nums):
            
            #leftmost element should be smaller 
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            # when we move window remove leftmost element
            if l > dq[0]:
                dq.popleft()
                
            #when r reaches len of k then update result and move the window
            if (r + 1) >= k:
                result.append(nums[dq[0]])
                l +=1
            r +=1
        return result