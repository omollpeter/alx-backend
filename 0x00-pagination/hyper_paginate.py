#!/usr/bin/python3

from math import ceil

def paginate_with_hypermedia(dataset, page, page_size, base_url):
    """
    Paginate a dataset and provide hypermedia metadata.

    :param dataset: The complete dataset (a list of items).
    :param page: The page number to retrieve (1-based index).
    :param page_size: The number of items per page.
    :param base_url: The base URL to use for generating pagination links.
    :return: A dictionary containing the paginated data and hypermedia metadata.
    """
    total_items = len(dataset)
    total_pages = ceil(total_items / page_size)

    if page < 1 or page > total_pages or page_size < 1:
        return {
            "error": "Invalid page or page size"
        }
    
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    items = dataset[start_index:end_index]

    # Generate links for pagination
    links = {
        "self": f"{base_url}?page={page}&page_size={page_size}",
        "first": f"{base_url}?page=1&page_size={page_size}",
        "last": f"{base_url}?page={total_pages}&page_size={page_size}"
    }

    if page > 1:
        links["prev"] = f"{base_url}?page={page - 1}&page_size={page_size}"
    if page < total_pages:
        links["next"] = f"{base_url}?page={page - 1}&page_size={page_size}"

    # Create the response with metadata
    return {
        "page": page,
        "page_size": page_size,
        "total_items": total_items,
        "total_pages": total_pages,
        "items": items,
        "links": links
    }


data = list(range(1, 1000))
base_url = "https://example.com/api/items"
result = paginate_with_hypermedia(data, 3, 20, base_url)

print(result)
