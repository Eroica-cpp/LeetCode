#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 3, 2015
# Question: 026-Remove-Duplicates-from-Sorted-Array
# Link:     https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# ==============================================================================
# Given a sorted array, remove the duplicates in place such that each element 
# appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this in place with 
# constant memory.
# 
# For example,
# Given input array nums = [1,1,2],
# 
# Your function should return length = 2, with the first two elements of nums 
# being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
# ==============================================================================
# Method: One pass
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==============================================================================

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        size = len(A)
        if size <= 1:
            return size
        ptr = 0
        for i in range(size-1):
            if A[i] != A[i+1]:
                A[ptr] = A[i]
                ptr += 1
            if i+2 == size:
                A[ptr] = A[i+1]
                ptr += 1
        return ptr