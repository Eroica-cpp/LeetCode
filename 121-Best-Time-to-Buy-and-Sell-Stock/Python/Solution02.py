#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jul 7, 2015
# Question: 121-Best-Time-to-Buy-and-Sell-Stock
# Link:     https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# ==============================================================================
# Say you have an array for which the ith element is the price of a given stock 
# on day i.
# 
# If you were only permitted to complete at most one transaction (ie, buy one 
# and sell one share of the stock), design an algorithm to find the maximum 
# profit.
# ==============================================================================
# Method: DP
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==============================================================================

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        size = len(prices)
        if size <= 1:
            return 0

        dp = [0] * size
        minVal = prices[0]
        for i in xrange(1, size):
            dp[i] = max(dp[i-1], prices[i]-minVal)
            minVal = prices[i] if prices[i] < minVal else minVal

        return dp[-1]
