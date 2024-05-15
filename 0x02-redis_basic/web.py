#!/usr/bin/env python3
'''A module with tools for request caching and tracking.'''
import requests
import redis
from functools import wraps


# Initialize Redis client
r = redis.Redis(host='localhost', port=6379, db=0)


def cache_page(func):
    """Decorator to cache the page and track URL access count"""
    @wraps(func)
    def wrapper(url):
        # Increase the access count for the URL
        count_key = f"count:{url}"
        r.incr(count_key)

        # Check if the page content is cached
        cache_key = f"cache:{url}"
        cached_page = r.get(cache_key)
        if cached_page:
            return cached_page.decode('utf-8')

        # If not cached, fetch the page content
        page_content = func(url)

        # Cache the page content with an expiration time of 10 seconds
        r.setex(cache_key, 10, page_content)
        return page_content

    return wrapper


@cache_page
def get_page(url: str) -> str:
    """Fetch the HTML content of a URL and return it"""
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    print(get_page('http://slowwly.robertomurray.co.uk'))
