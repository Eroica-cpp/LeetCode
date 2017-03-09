#!/usr/bin/python
"""
====================================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 12, 2015
Question: 146-LRU-Cache
Link:     https://leetcode.com/problems/lru-cache/
====================================================================================
Design and implement a data structure for Least Recently Used (LRU) cache. It 
should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists 
in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. 
When the cache reached its capacity, it should invalidate the least recently used 
item before inserting a new item.
====================================================================================
Method: a two direction linked list; a hash map
====================================================================================
"""

class CacheNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cacheMap = {}
        

    # @return an integer
    def get(self, key):
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
