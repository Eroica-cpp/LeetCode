#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 5, 2015
Question: 123-Best-Time-to-Buy-and-Sell-Stock-III
Link:     https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
==============================================================================
Say you have an array for which the ith element is the price of a given 
stock on day i.

Design an algorithm to find the maximum profit. You may complete at most 
two transactions.

Note:
You may not engage in multiple transactions at the same time 
(ie, you must sell the stock before you buy again).
==============================================================================
Method: Two passes
Time Complexity: O(n)
Space Complexity: O(1)
==============================================================================
"""

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        size = len(prices)
        minIdx = maxIdx = tmpMinIdx = 0
        minVal, maxVal = float('inf'), 0

        for i in xrange(size):
            if prices[i] < minVal: 
                minVal = prices[i]
                tmpMinIdx = i
            if prices[i] - minVal > maxVal:
                maxVal = prices[i] - minVal
                maxIdx = i
                minIdx = tmpMinIdx

        profit = maxVal
        minVal, maxVal = float('inf'), 0

        for i in range(0,minIdx)+range(maxIdx+1,size):
            if prices[i] < minVal: minVal = prices[i]
            if prices[i] - minVal > maxVal: maxVal = prices[i] - minVal

        profit += maxVal
        return profit

if __name__ == '__main__':
    prices = [1,10,20,3,4,5, 1, 10, 2]
    prices = [2,4,1]
    prices = [6,1,3,2,4,7]
    print Solution().maxProfit(prices)