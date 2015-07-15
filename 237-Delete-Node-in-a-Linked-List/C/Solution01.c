/*
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 15, 2015
Question: 237-Delete-Node-in-a-Linked-List
Link:     https://leetcode.com/problems/delete-node-in-a-linked-list/
==============================================================================
Write a function to delete a node (except the tail) in a singly linked list, 
given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node 
with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.
==============================================================================
*/

#include <stdlib.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

void deleteNode(struct ListNode* node) {
    struct ListNode *tmp = node->next;
    node->val = node->next->val;
    node->next = node->next->next;
    free(tmp);
}

int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}