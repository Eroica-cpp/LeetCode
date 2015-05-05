#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 2, 2015
# Question: 160-Intersection-of-Two-Linked-Lists
# Link:     https://leetcode.com/problems/intersection-of-two-linked-lists/
# ==============================================================================
# Write a program to find the node at which the intersection of two singly 
# linked lists begins.
# ==============================================================================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param two ListNodes
	# @return the intersected ListNode
	def getIntersectionNode(self, headA, headB):
		lengthA, lengthB = 0, 0
		p1, p2 = headA, headB
		while p1:
			p1 = p1.next
			lengthA += 1
		while p2:
			p2 = p2.next
			lengthB += 1
			
		p1, p2 = headA, headB
		if lengthA > lengthB:
			counter = lengthA - lengthB
			while counter > 0:
				p1 = p1.next
				counter -= 1
		else:
			counter = lengthB - lengthA
			while counter > 0:
				p2 = p2.next
				counter -= 1

		while p1 and p2 and p1.val != p2.val:
			p1 = p1.next
			p2 = p2.next
		return p1