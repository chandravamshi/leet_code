# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        m = (1 + r) // 2
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
