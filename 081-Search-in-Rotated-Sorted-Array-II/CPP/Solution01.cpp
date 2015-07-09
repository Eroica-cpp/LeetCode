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
Method: Binary Search
Time Complexity: O(log n)
Space Complexity: O(1)
Note: 
1. An extension of question #033-Search-in-Rotated-Sorted-Array
2. Carefully handle '>' or '>=' and '+ 1' or '- 1' cases
==============================================================================
*/

#include <vector>

using namespace std;

class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return true;
            if (nums[left] < nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) right = mid - 1;
                else left = mid + 1;
            } else if (nums[left] > nums[mid]) {
                if (nums[mid] < target && target <= nums[right]) left = mid + 1;
                else right = mid - 1;
            } else {
                left ++;
            }
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