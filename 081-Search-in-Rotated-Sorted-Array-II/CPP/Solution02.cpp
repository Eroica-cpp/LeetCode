/*
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     May 7, 2015
Question: 081-Search-in-Rotated-Sorted-Array-II
Link:     https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
==============================================================================
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
==============================================================================
Method: loop; brute force
Time Complexity: O(n)
Space Complexity: O(1)
==============================================================================
*/

#include <vector>

using namespace std;

class Solution {
public:
    bool search(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i ++) {
            if (nums[i] == target) return true;
        }
        return false;
    }
};

/* Unit Test */
int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}