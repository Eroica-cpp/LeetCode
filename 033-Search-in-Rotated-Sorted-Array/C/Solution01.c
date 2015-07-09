/*
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 9, 2015
Question: 033-Search-in-Rotated-Sorted-Array
Link:     https://leetcode.com/problems/search-in-rotated-sorted-array/
==============================================================================
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its 
index, otherwise return -1.

You may assume no duplicate exists in the array.
==============================================================================
Method: binary search
Time Complexity: O(log n)
Space Complexity: O(1)
Note: it is tricky, pay attention to the boundary conditions
==============================================================================
*/

int search(int* nums, int numsSize, int target) {
    int left = 0;
    int right = numsSize - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) return mid;
        if (nums[left] <= nums[mid]) {
            if (nums[left] <= target && target < nums[mid]) right = mid - 1;
            else left = mid + 1;
        } else {
            if (nums[mid] < target && target <= nums[right]) left = mid + 1;
            else right = mid - 1;
        }
    }
    return -1;
}

/* Unit Test */
int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}