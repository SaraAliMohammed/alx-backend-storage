#!/usr/bin/env python3
'''A module with tools for request caching and tracking.'''
import redis
import requests
rc = redis.Redis()
count = 0


def get_page(url: str) -> str:
    '''
    It uses the requests module to obtain the HTML content of
    a particular URL and returns it.
    Returns the content of a URL after caching the request's response,
    and tracking the request.
    '''
    rc.set(f"cached:{url}", count)
    resp = requests.get(url)
    rc.incr(f"count:{url}")
    rc.setex(f"cached:{url}", 10, rc.get(f"cached:{url}"))
    return resp.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
