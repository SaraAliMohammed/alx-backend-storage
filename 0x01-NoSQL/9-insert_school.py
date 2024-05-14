#!/usr/bin/env python3
""" Module of insert_school function """


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based on kwargs.
    mongo_collection will be the pymongo collection object.
    Returns the new _id """
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id
