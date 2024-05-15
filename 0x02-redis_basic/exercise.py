#!/usr/bin/env python3
""" Module of Cache class """
import redis
import uuid
from typing import Union


class Cache:
    """ Represents Cache class """
    def __init__(self) -> None:
        """
        Method that store an instance of the Redis client
        as a private variable named _redis
        (using redis.Redis()) and flush the instance using flushdb.
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key (e.g. using uuid),
        store the input data in Redis using the random key and
        return the key.
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
