class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        res = [-1]*len(nums1)
        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i]),n):
                if nums2[j] > nums1[i]:
                    res[i] = nums2[j]
                    break
        return res

    
        