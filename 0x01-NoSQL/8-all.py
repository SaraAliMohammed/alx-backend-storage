#!/usr/bin/env python3
""" Module of list_all function """


def list_all(mongo_collection):
    """ Lists all documents in a collection """
    num_documents = mongo_collection.count_documents({})
    if num_documents == 0:
        return []
    return mongo_collection.find()
