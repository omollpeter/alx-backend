#!/usr/bin/env python3
"""
This module contains LRUCache class that inherits from BaseCaching
The class defines implementation for LRU caching replacement policy
"""


BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    Defines LRUCache class
    """

    def __init__(self):
        """
        Initializes instance attributes
        """
        super().__init__()
        self.trkr = []

    def put(self, key, item):
        """
        Adds data to a dict like cache
        Replaces the oldest data if cache is full
        """
        if key and item:
            if key in self.cache_data.keys():
                idx = self.trkr.index(key)
                self.trkr.remove(key)
                self.trkr.append(key)
                self.cache_data[key] = item
                return
            if len(self.cache_data) < self.MAX_ITEMS:
                self.trkr.append(key)
                self.cache_data[key] = item
            else:
                discard = self.trkr.pop(0)
                print("DISCARD:", discard)
                del self.cache_data[discard]

                self.trkr.append(key)
                self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves data from the cache using the key
        """
        if key:
            if key in self.cache_data.keys():
                idx = self.trkr.index(key)
                self.trkr.remove(key)
                self.trkr.append(key)
            return self.cache_data.get(key)
        return None
