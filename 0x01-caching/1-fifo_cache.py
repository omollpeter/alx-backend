#!/usr/bin/env python3
"""
This module contains FIFOCache class that inherits from BaseCaching
The class defines implementation for FIFO caching replacement policy
"""


BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    Defines FIFOCache class
    """

    def __init__(self):
        """
        Initializes instance attributes
        """
        super().__init__()
        self.tracker = []

    def put(self, key, item):
        """
        Adds data to a dict like cache
        Replaces the oldest data if cache is full
        """
        if key and item:
            if len(self.cache_data) < self.MAX_ITEMS:
                self.tracker.append(key)
                self.cache_data[key] = item
            else:
                discard = self.tracker.pop(0)
                print("DISCARD:", discard)
                del self.cache_data[discard]

                self.tracker.append(key)
                self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves data from the cache using the key
        """
        if key:
            return self.cache_data.get(key)
        return None
