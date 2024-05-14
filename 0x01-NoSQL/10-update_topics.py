#!/usr/bin/env python3
""" Module of update_topics function """


def update_topics(mongo_collection, name, topics):
    """ Changes all topics of a school document based on the name.
    name (string) will be the school name to update.
    topics (list of strings) will be the list of topics approached
    in the school """
    new_query = {"name": name}
    new_topics = {"$set": {"topics": topics}}

    mongo_collection.update_many(new_query, new_topics)
