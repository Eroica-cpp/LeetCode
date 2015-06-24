#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jun 24, 2015
Question: 133-Clone-Graph
Link:     https://leetcode.com/problems/clone-graph/
==============================================================================
Clone an undirected graph. Each node in the graph contains a label and a list 
of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and 
each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as 
separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a 
self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
==============================================================================
Method: DFS
Time Complexity: O(n)
Space Complexity: O(n)
==============================================================================
"""

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        nodeMap = {}
        return self.cloneNode(node, nodeMap)

    def cloneNode(self, node, nodeMap):
        if not node:
            return

        if nodeMap.has_key(node):
            return nodeMap[node]

        clone = UndirectedGraphNode(node.label)
        nodeMap[node] = clone
        for neighbor in node.neighbors:
            clone.neighbors.append(self.cloneNode(neighbor, nodeMap))

        return clone
