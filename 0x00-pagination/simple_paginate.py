#!/usr/bin/env python3
def paginate(dataset, page, page_size):
    """
    Paginate a dataset.

    :param dataset: The complete dataset (a list of items).
    :param page: The page number to retrieve (1-based index).
    :param page_size: The number of items per page.
    :return: A list of items for the current page.
    """

    if page < 1 or page_size < 1:
        raise ValueError("Page and page size must be greater than 0")
    
    start = (page - 1) * page_size
    end = start + page_size

    return dataset[start:end]

print(paginate(list(range(100)), 3, 10))
