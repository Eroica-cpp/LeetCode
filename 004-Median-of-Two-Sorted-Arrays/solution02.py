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
# Method: Combine and Sort
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Note: Try binary search next time
# ==============================================================================

class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        combine = sorted(nums1 + nums2)
        
        if not combine:
            return
        
        size = len(combine)
        return (float(combine[size/2-1])+float(combine[size/2]))/2 if size%2 == 0 else combine[size/2]

if __name__ == '__main__':
    nums1, nums2 = [2], [3]
    print Solution().findMedianSortedArrays(nums1, nums2)