#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 15, 2015
# Question: 179-Largest-Number
# Link:     https://leetcode.com/problems/largest-number/
# ==============================================================================
# Given a list of non negative integers, arrange them such that they form the 
# largest number.
# 
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
# 
# Note: The result may be very large, so you need to return a string instead 
# of an integer.
# ==============================================================================
# Method: quick sort
# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Note: 
# 1. quick sort reference: http://hetland.org/coding/python/quicksort.html
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        size = len(nums)
        nums = [str(k) for k in nums]
        for i in xrange(size,-1,-1):
            for j in xrange(0, i-1):
                if int(nums[j]+nums[j+1]) < int(nums[j+1]+nums[j]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return str(int("".join(nums)))

    def partition(self, list, start, end):
        pivot = list[end]                          
        bottom = start-1                           
        top = end                                  

        done = 0
        while not done:                            

            while not done:                        
                bottom = bottom+1                  

                if bottom == top:                  
                    done = 1                       
                    break

                if list[bottom] > pivot:           
                    list[top] = list[bottom]       
                    break                          

            while not done:                        
                top = top-1                       
                
                if top == bottom:                  
                    done = 1                       
                    break

                if list[top] < pivot:              
                    list[bottom] = list[top]       
                    break                         

        list[top] = pivot                          
        return top                                

    def quicksort(self, nums, start, end):
        if start < end:                            
            split = self.partition(nums, start, end)    
            self.quicksort(nums, start, split-1)        
            self.quicksort(nums, split+1, end)
        else:
            return

if __name__ == '__main__':
    nums = [3, 30, 34, 5, 9]
    nums = [120,12]
    nums = [0,0,1]
    print Solution().quicksort(nums, 0 , len(nums))
    print nums