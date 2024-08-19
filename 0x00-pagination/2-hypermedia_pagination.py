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
from math import ceil


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
        assert page > 0 and type(page) is int, "Page must be greater than 0"
        assert type(page_size) is int
        assert page_size > 0, "Page size must be greater than 0"

        index_rng = index_range(page, page_size)
        start, end = index_rng

        data = self.__dataset
        if not data:
            data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a dictionary containing page_size, page, data, next_page,
        prev_page, total_pages
        """
        data = self.get_page(page, page_size)
        prev_page = page - 1 if page > 1 else None
        total_pages = ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
