/* ===========================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 3, 2015
Question: 121-Best-Time-to-Buy-and-Sell-Stock
Link:     https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
==============================================================================
Say you have an array for which the ith element is the price of a given stock 
on day i.

If you were only permitted to complete at most one transaction (ie, buy one 
and sell one share of the stock), design an algorithm to find the maximum 
profit.
==============================================================================
Time Complexity: O(n)
Space Complexity: O(1)
============================================================================== */

public class Solution01 {
    public static int maxProfit(int[] prices) {
        int minVal = java.lang.Integer.MAX_VALUE;
        int maxVal = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minVal) minVal = prices[i];
            if (prices[i]-minVal > maxVal) maxVal = prices[i] - minVal;
        }
        return maxVal;
    }
}