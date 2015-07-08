// ==============================================================================
// Author:   Tao Li (taoli@ucsd.edu)
// Date:     Jul 8, 2015
// Question: 219-Contains-Duplicate-II
// Link:     https://leetcode.com/problems/contains-duplicate-ii/
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
// Method: use extra space to store appear times
// Time Complexity: O(n)
// Space Complexity: O(n)
// Note: 
// 1. try not use extra space next time
// 2. this solution would fail in case of having negative integer elements.
// ==============================================================================

#include <stdlib.h>
#include <stdio.h>

int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int len = nums[numsSize-1] + 1;
    int* counter;
    counter = (int*) malloc(sizeof(int) * len);

    int index = 0, i;
    for (i = 0; i < numsSize; i++) {
        if (counter[nums[i]] < 2) {
            nums[index++] = nums[i];
            counter[nums[i]] ++;
        }
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