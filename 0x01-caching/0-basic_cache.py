#!/usr/bin/env python3
"""
This module contains BasicCache class that inherits from BaseCaching
"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    Defines BasicCache class
    """

    def __init__(self):
        """
        Initializes instance attributes
        """
        super().__init__()

    def put(self, key, item):
        """
        For inserting values to dict like cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves data from the cache using the key
        """
        if key:
            return self.cache_data.get(key)
        return None
