#!/usr/bin/env python3
"""
This module contains a function that returns a tuple containing start
index and end index corresponding to range of indexes to return in a 
list

It also contains a class definition for Server
"""


import csv
import math
from typing import List



def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing start index
    and end index corresponding to range of indexes to return in a list
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a subset of list data to emulate pagination
        """
        assert page > 0 and type(page) == int, "Page must be greater than 0"
        assert type(page_size) == int
        assert page_size > 0, "Page size must be greater than 0"

        index_rng = index_range(page, page_size)
        start, end = index_rng

        data = self.__dataset
        if not data:
            data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]
