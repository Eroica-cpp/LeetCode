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
Method: 2D DP
Time Complexity: O(n)
Space Complexity: O(n)
Note: 
1. greedy approach - find the top two best transaction - is wrong, consider 
a counterexample: [6,1,3,2,4,7]. 
2. refer to DP solution in #121-Best-Time-to-Buy-and-Sell-Stock
Reference: 
1. http://segmentfault.com/a/1190000002565570
2. http://liangjiabin.com/blog/2015/04/leetcode-best-time-to-buy-and-sell-stock.html
==============================================================================
"""

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        size = len(prices)
        if size <= 1:
            return 0

        left = [0] * size
        right = [0] * size

        minVal = prices[0]
        for i in xrange(1, size):
            left[i] = max(left[i-1], prices[i]-minVal)
            minVal = min(minVal, prices[i])

        maxVal = prices[-1]
        for j in xrange(2, size+1):
            right[-j] = max(right[-j+1], maxVal-prices[-j])
            maxVal = max(maxVal, prices[-j])

        res = 0
        for i in xrange(size):
            res = max(res, left[i]+right[i])
        return res

if __name__ == '__main__':
    prices = [1,10,20,3,4,5, 1, 10, 2]
    prices = [2,4,1]
    prices = [6,1,3,2,4,7]
    print Solution().maxProfit(prices)
