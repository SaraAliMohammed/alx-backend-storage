#!/usr/bin/env python3
'''A module with tools for request caching and tracking.'''
import redis
import requests

# Initialize Redis client
rc = redis.Redis()


def get_page(url: str) -> str:
    '''
    It uses the requests module to obtain the HTML content of
    a particular URL and returns it.
    Returns the content of a URL after caching the request's response,
    and tracking the request.
    '''
    # Check if the content is already cached
    cached_content = rc.get(f"cached:{url}")
    if cached_content:
        return cached_content.decode('utf-8')

    # If not cached, make the request
    resp = requests.get(url)

    # Increment the access count for the URL
    rc.incr(f"count:{url}")

    # Cache the response content with an expiration time of 10 seconds
    rc.setex(f"cached:{url}", 10, resp.text)

    return resp.text


if __name__ == "__main__":
    url =
    'http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com'
    print(get_page(url))
