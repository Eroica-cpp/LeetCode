// ==============================================================================
// Author:   Tao Li (taoli@ucsd.edu)
// Date:     Jul 8, 2015
// Question: 080-Remove-Duplicates-from-Sorted-Array-II
// Link:     https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
// ==============================================================================
// Follow up for "Remove Duplicates":
// What if duplicates are allowed at most twice?
// 
// For example,
// Given sorted array nums = [1,1,1,2,2,3],
// 
// Your function should return length = 5, with the first five elements of nums 
// being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
// ==============================================================================
// Method: One pass without extra space
// Time Complexity: O(n)
// Space Complexity: O(1)
// ==============================================================================

#include <stdio.h>

int removeDuplicates(int* nums, int numsSize) {
    if (numsSize <= 2) return numsSize;

    int index = 2, i;
    for (i = 2; i < numsSize; i ++) {
        if (nums[i] != nums[index-2])
            nums[index++] = nums[i];
    }
    return index;
}

/* Unit Test */
#define N 7
int main(int argc, char const *argv[])
{
    int a[N] = {1,1,1,2,2,2,3};
    int len = removeDuplicates(a, N);
    int i = 0;
    for (; i < N; i++)
        printf("%d\n", a[i]);
    printf("len = %d\n", len);
    
    return 0;
}