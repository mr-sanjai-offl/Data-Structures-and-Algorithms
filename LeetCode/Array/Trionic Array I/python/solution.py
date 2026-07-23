class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3:
            return False
        p = 0
        while p + 1 < n and nums[p] < nums[p + 1]:
            p += 1

        if p == 0 or p == n - 1:
            return False
 
        q = p
        while q + 1 < n and nums[q] > nums[q + 1]:
            q += 1

        if q == p or q == n - 1:
            return False

        while q + 1 < n and nums[q] < nums[q + 1]:
            q += 1

        return q == n - 1
