#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 7, 2015
# Question: 081-Search-in-Rotated-Sorted-Array-II
# Link:     https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# ==============================================================================
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
# 
# Would this affect the run-time complexity? How and why?
# 
# Write a function to determine if a given target is in the array.
# ==============================================================================
# Method: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Note: 
# 1. An extension of question #033-Search-in-Rotated-Sorted-Array
# 2. Carefully handle '>' or '>=' and '+ 1' or '- 1' cases
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return False
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return True
            if nums[mid] > nums[low]:
                if nums[mid] > target and nums[low] <= target:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < nums[low]:
                if nums[mid] < target and nums[high] >= target:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                low += 1
        return False

if __name__ == '__main__':
    print Solution().search([2, 1], 1)