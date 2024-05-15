#!/usr/bin/env python3
""" Module of Cache class """
import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None
            ) -> Union[str, bytes, int, float]:
        """
        Takes a key string argument and an optional Callable argument named fn.
        This callable will be used to convert the data back
        to the desired format.
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """ Retrieves a string value from a Redis data storage. """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """ Retrieves an integer value from a Redis data storage. """
        return self.get(key, lambda x: int(x))
