#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 5, 2015
# Question: 122-Best-Time-to-Buy-and-Sell-Stock-II
# Link:     https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# ==============================================================================
# Say you have an array for which the ith element is the price of a given stock 
# on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many 
# transactions as you like (ie, buy one and sell one share of the stock multiple 
# times). However, you may not engage in multiple transactions at the same time 
# (ie, you must sell the stock before you buy again).
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
        total = 0
        for i in range(len(prices)-1):
            total += prices[i+1]-prices[i] if prices[i+1]-prices[i] > 0 else 0
        return total