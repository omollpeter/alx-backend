#!/usr/bin/env python3
"""
This module contains a function that returns a tuple containing start
index and end index corresponding to range of indexes to return in a
list
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing start index
    and end index corresponding to range of indexes to return in a list
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
