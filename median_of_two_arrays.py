from ast import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        total_len = m + n
        half_len = (total_len + 1) // 2

        while left <= right:
            i = (left + right) // 2
            j = half_len - i

            max_left1 = nums1[i-1] if i > 0 else float('-inf')
            min_right1 = nums1[i] if i < m else float('inf')
            max_left2 = nums2[j-1] if j > 0 else float('-inf')
            min_right2 = nums2[j] if j < n else float('inf')

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (total_len % 2) != 0:
                    return float(max(max_left1, max_left2))
                return ((max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0 )
            elif max_left1 > min_right2:
                right = i - 1
            else:
                left = i + 1
        return 0.0
