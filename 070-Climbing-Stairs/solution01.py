#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 2, 2015
# Question: 070-Climbing-Stairs
# Link:     https://leetcode.com/problems/climbing-stairs/
# ==============================================================================
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways 
# can you climb to the top?
# ==============================================================================
# Method: Recursion
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
# Note: an OK solution but "Time Limit Exceeded"
# ==============================================================================

class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2) 

if __name__ == '__main__':
    print Solution().climbStairs(5)