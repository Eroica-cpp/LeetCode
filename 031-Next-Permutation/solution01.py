#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 24, 2015
# Question: 031-Next-Permutation
# Link:     https://leetcode.com/problems/next-permutation/
# ==============================================================================
# Implement next permutation, which rearranges numbers into the 
# lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the 
# lowest possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place, do not allocate extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and 
# its corresponding outputs are in the right-hand column.
# 1,2,3 -> 1,3,2
# 3,2,1 -> 1,2,3
# 1,1,5 -> 1,5,1
# ==============================================================================
# Time Complexity: O(n)
# Space Complexity: O(1)
# Note:
# 1. Reference http://fisherlei.blogspot.com/2012/12/leetcode-next-permutation.html
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):

        size = len(nums)

        i = 0
        for i in xrange(1, size+1):
            if i+1 > size or nums[-(i+1)] < nums[-i]:
                break

        j = 0
        for j in xrange(1, i+1):
            if i+1 > size:
                break
            if nums[-j] > nums[-(i+1)]:
                nums[-j], nums[-(i+1)] = nums[-(i+1)], nums[-j]
                break

        k = 0
        for k in xrange(1, (i+1)/2+1):
            nums[-k], nums[-(i-k+1)] = nums[-(i-k+1)], nums[-k]

if __name__ == '__main__':
    # nums = [1, 2, 3]
    # nums = [1, 1, 5]
    # nums = [3, 2, 1]
    # nums = [1,3,2]
    nums = [6, 8, 7, 4, 3, 2]
    Solution().nextPermutation(nums)
    print nums