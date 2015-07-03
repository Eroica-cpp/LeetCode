// ==============================================================================
// Author:   Tao Li (taoli@ucsd.edu)
// Date:     Jul 3, 2015
// Question: 122-Best-Time-to-Buy-and-Sell-Stock-II
// Link:     https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
// ==============================================================================
// Say you have an array for which the ith element is the price of a given stock 
// on day i.

// Design an algorithm to find the maximum profit. You may complete as many 
// transactions as you like (ie, buy one and sell one share of the stock multiple 
// times). However, you may not engage in multiple transactions at the same time 
// (ie, you must sell the stock before you buy again).
// ==============================================================================
// Time Complexity: O(n)
// Space Complexity: O(1)
// ==============================================================================

public class Solution01 {
    public int maxProfit(int[] prices) {
        if (prices.length == 0) return 0;

        int profit = 0;
        for (int i = 0; i < prices.length-1; i++) {
            if (prices[i+1] - prices[i] > 0) profit += prices[i+1] - prices[i];
        }
        return profit;
    }
}