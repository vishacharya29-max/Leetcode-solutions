class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 1. Combine and sort
        merged = sorted(nums1 + nums2)
        n = len(merged)
        mid = n // 2
        
        # 2. If odd, return the exact middle number
        if n % 2 != 0:
            return float(merged[mid])
        
        # 3. If even, return the average of the two middle numbers
        return (merged[mid - 1] + merged[mid]) / 2.0
