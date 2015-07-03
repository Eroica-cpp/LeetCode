#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 5, 2015
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
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==============================================================================

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        minVal = float('inf')
        diff = 0
        for i in range(len(prices)):
            if prices[i] < minVal:
                minVal = prices[i]
            if prices[i] - minVal > diff:
                diff = prices[i] - minVal
        return diff

