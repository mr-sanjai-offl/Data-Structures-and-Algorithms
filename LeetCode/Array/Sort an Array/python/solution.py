class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            L = nums[:mid]
            R = nums[mid:]

            sortedLeft = mergeSort(L)
            sortedRight = mergeSort(R)

            return merge(sortedLeft, sortedRight)

        def merge(l, r):
            i = j = 0
            result = []

            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    result.append(l[i])
                    i+=1
                else:
                    result.append(r[j])
                    j+=1
            result.extend(l[i:])
            result.extend(r[j:])
            return result
        return mergeSort(nums)