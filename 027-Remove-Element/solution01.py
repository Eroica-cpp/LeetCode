#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 3, 2015
# Question: 027-Remove-Element
# Link:     https://leetcode.com/problems/remove-element/
# ==============================================================================
# Given an array and a value, remove all instances of that value in place and 
# return the new length.
# 
# The order of elements can be changed. It doesn't matter what you leave beyond 
# the new length.
# ==============================================================================
# Method: Two pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==============================================================================

class Solution:
    # @param A, a list of integers
    # @param elem, an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        counter = 0
        for i in range(len(A)):
            if A[i] != elem:
                A[counter] = A[i] 
                counter += 1
        return counter
