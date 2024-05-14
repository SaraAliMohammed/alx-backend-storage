#!/usr/bin/env python3
""" Module of schools_by_topic function """


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of school having a specific topic.
    topic (string) will be topic searche."""
    documents = mongo_collection.find({"topics": topic})
    docs_list = [d for d in documents]
    return docs_list
