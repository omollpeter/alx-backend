#!/usr/bin/env python3
"""
This module contains LIFOCache class that inherits from BaseCaching
The class defines implementation for LIFO caching replacement policy
"""


BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
    Defines LIFOCache class
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
                self.trkr[idx], self.trkr[3] = self.trkr[3], self.trkr[idx]
                self.cache_data[key] = item
                return
            if len(self.cache_data) < self.MAX_ITEMS:
                self.trkr.append(key)
                self.cache_data[key] = item
            else:
                discard = self.trkr.pop(3)
                print("DISCARD:", discard)
                del self.cache_data[discard]

                self.trkr.append(key)
                self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves data from the cache using the key
        """
        if key:
            return self.cache_data.get(key)
        return None
