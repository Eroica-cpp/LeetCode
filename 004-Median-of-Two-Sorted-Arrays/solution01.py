#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 1, 2015
# Question: 004-Median-of-Two-Sorted-Arrays
# Link:     https://leetcode.com/problems/median-of-two-sorted-arrays/
# ==============================================================================
# There are two sorted arrays nums1 and nums2 of size m and n respectively. 
# Find the median of the two sorted arrays. The overall run time complexity 
# should be O(log (m+n)).
# ==============================================================================
# Method: Traverse, Naive Method
# Time Complexity: O(m+n)
# Space Complexity: O(1)
# ==============================================================================

class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1 and not nums2:
            return 

        p1 = p2 = 0
        m, n = len(nums1), len(nums2)
        last = med = 0

        while p1 + p2 <= (m + n) / 2:
            last = med
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    med = nums1[p1]
                    p1 += 1
                else:
                    med = nums2[p2]
                    p2 += 1
            elif p1 < m:
                med = nums1[p1]
                p1 += 1
            else:
                med = nums2[p2]
                p2 += 1

        if (m+n) % 2 == 0: 
            med = (float(last) + float(med)) / 2

        return med

if __name__ == '__main__':
    nums1, nums2 = [3], [1, 3]
    print Solution().findMedianSortedArrays(nums1, nums2)