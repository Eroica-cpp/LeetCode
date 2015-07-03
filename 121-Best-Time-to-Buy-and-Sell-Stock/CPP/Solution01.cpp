// ==============================================================================
// Author:   Tao Li (taoli@ucsd.edu)
// Date:     Jul 3, 2015
// Question: 121-Best-Time-to-Buy-and-Sell-Stock
// Link:     https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// ==============================================================================
// Say you have an array for which the ith element is the price of a given stock 
// on day i.

// If you were only permitted to complete at most one transaction (ie, buy one 
// and sell one share of the stock), design an algorithm to find the maximum 
// profit.
// ==============================================================================
// Time Complexity: O(n)
// Space Complexity: O(1)
// ==============================================================================

#include <iostream>
#include <vector>
#include <limits>

using namespace std;

#define MAX_INT numeric_limits<int>::max()
#define MIN_INT numeric_limits<int>::min()

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxVal = 0;
        int minVal = MAX_INT;
        for (int i = 0; i < prices.size(); i++) {
            if (prices[i] < minVal) minVal = prices[i];
            if (prices[i] - minVal > maxVal) maxVal = prices[i] - minVal;
        }
        return maxVal;
    }
};

int main() {
    int array[] = {1,2,3};
    vector<int> v(array, array+sizeof(array)/sizeof(array[0]));
    
    Solution s;
    cout << s.maxProfit(v) << endl;
    
    return 0;
}